"""Homework 10.1."""
import asyncio
import json
from concurrent.futures import ProcessPoolExecutor
from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple, Union
from xml.etree import ElementTree

import aiofiles
import aiohttp
import requests
from bs4 import BeautifulSoup


async def fetch_response(url: str) -> str:
    """Asynchronously fetch response."""
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()


def get_href_from_main_page(soup: BeautifulSoup) -> List:
    """Get list of hyper references from main pages of businessinsider."""
    res = []
    i = 0
    for tag in soup.find_all("a"):
        href, cls, title = tag.get("href"), tag.get("class"), tag.get("title")
        if href.startswith("/stocks/") and title and not cls:
            i += 1
            res.append([title, main_url + href])
    return res


def get_year_growth_from_main_page(soup: BeautifulSoup) -> List:
    """Get year growth from main page."""
    tags = soup.find_all("span")
    y_growth = []
    for i, tag in enumerate(tags):
        if tag.get("format"):
            y_growth.append(tags[i + 6].text)
    return y_growth


def get_curr_usd_rate() -> Optional[float]:
    """Get current USA dollar rate in rubles from centroban server."""
    response = requests.get("http://www.cbr.ru/scripts/XML_daily.asp")
    tree = ElementTree.fromstring(response.content)
    for child in tree:
        if child.attrib["ID"] == "R01235":
            usd_rate = float(child[4].text.replace(",", "."))
            break
    return usd_rate


def write_json(data: List[Dict], file: str) -> None:
    """Write data to json file."""
    with open(file, "w") as f:
        f.write(json.dumps(data))


async def async_write_json(data: List[Dict], filename: str) -> None:
    """Asynchronously write data to json file."""
    async with aiofiles.open(f"{filename}.json", "w") as f:
        await f.write(json.dumps(data, indent=4))


async def get_async_responses(url_s: List[str]) -> Tuple:
    """Asynchronously get responses from main pages."""
    tasks = [asyncio.create_task(fetch_response(url)) for url in url_s]
    return await asyncio.gather(*tasks)


@dataclass
class StockData:
    """Dataclass of stock data."""

    price: List[Dict]
    pe: List[Dict]
    profit: List[Dict]
    growth: List[Dict]


def make_dict(name: str, code: str, item_name: str, item: Union[str, float]) -> Dict:
    """Return dict of values for single stock to be written in json."""
    return {"name": name, "code": code, item_name: item}


def get_name_code(soup: BeautifulSoup) -> Tuple:
    """Get name code of stock."""
    name = soup.find("span", {"class": "price-section__label"}).text.strip()
    code = soup.find("span", {"class": "price-section__category"}).text.strip()[8:]
    return name, code


def get_price(soup: BeautifulSoup) -> float:
    """Get price of stock."""
    _price = soup.find("span", {"class": "price-section__current-value"}).text
    return float(_price.replace(",", "")) * usd_rate


def get_profit(soup: BeautifulSoup) -> float:
    """Get and calculate potential profit for single stock."""
    tag_price_low = "snapshot__data-item snapshot__data-item--small"
    price_low_raw = soup.find_all("div", {"class": tag_price_low})[-1].text.split()[0]
    price_low = price_low_raw.replace(",", "")

    tag_p_h = (
        "snapshot__data-item snapshot__data-item--small snapshot__data-item--right"
    )
    _price_high_raw = soup.find_all("div", {"class": tag_p_h})
    _price_high_raw = _price_high_raw[-1].text.split()[0]
    price_high = _price_high_raw.replace(",", "")
    profit_ratio = (float(price_high) - float(price_low)) / float(price_low)
    return 100 * profit_ratio


def get_pe(soup: BeautifulSoup) -> float:
    """Get P/E for stock."""
    _pe_raw = soup.find_all("div", {"class": "snapshot__data-item"})
    _pe_raw = _pe_raw[8].text.split()[0]
    pe = _pe_raw.replace(",", "")
    return float(pe)


def parse_stock_page(html: str, y_growth: str) -> StockData:
    """Parse single stock page to get price, pe, profit, code, name."""
    soup = BeautifulSoup(html, "html.parser")

    name, code = get_name_code(soup)
    price = get_price(soup)
    profit = get_profit(soup)
    pe = get_pe(soup)

    stock_data = StockData([], [], [], [])
    stock_data.price.append(make_dict(name, code, "price", price))
    stock_data.pe.append(make_dict(name, code, "P_E", float(pe)))
    stock_data.profit.append(make_dict(name, code, "potential profit", profit))
    stock_data.growth.append(make_dict(name, code, "growth", float(y_growth[:-1])))

    return stock_data


def sort_by_item(data: List[Dict], item_name: str) -> List[Dict]:
    """Prepare data to be written. Sort and slice."""
    is_reverse = True

    if item_name == "P_E":
        is_reverse = False

    return sorted(data, key=lambda x: x[item_name], reverse=is_reverse)[:10]


async def main() -> None:
    """Get all data from main pages. Parse it. Get all data from single pages. Parse them. Combine all data."""
    main_html_pages = await get_async_responses(urls)

    soups = [BeautifulSoup(html, "html.parser") for html in main_html_pages]
    hrefs = []
    y_growths = []

    for soup in soups:
        href = get_href_from_main_page(soup)
        hrefs += href

        y_growth = get_year_growth_from_main_page(soup)
        y_growths += y_growth

    stock_urls = [stock_url for _, stock_url in hrefs]
    stock_htmls = await get_async_responses(stock_urls)

    with ProcessPoolExecutor(max_workers=10) as executor:
        data = executor.map(parse_stock_page, *(stock_htmls, y_growths))

    price = []
    p_e = []
    potential_profit = []
    growth = []
    for stock in data:
        price.append(stock.price[0])
        p_e.append(stock.pe[0])
        potential_profit.append(stock.profit[0])
        growth.append(stock.growth[0])

    all_info = [price, p_e, growth, potential_profit]
    filenames = ["price", "P_E", "growth", "potential profit"]
    all_data = [
        sort_by_item(info, filename) for info, filename in zip(all_info, filenames)
    ]

    write_files = [
        asyncio.create_task(async_write_json(data, filename))
        for data, filename in zip(all_data, filenames)
    ]
    await asyncio.gather(*write_files)


main_url = "https://markets.businessinsider.com"
urls = [main_url + f"/index/components/s&p_500?p={i}" for i in range(1, 11)]
usd_rate = get_curr_usd_rate()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
