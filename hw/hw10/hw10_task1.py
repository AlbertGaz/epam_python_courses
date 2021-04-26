"""Homework 10.1."""
import asyncio
import json
from concurrent.futures import ProcessPoolExecutor
from typing import Dict, List, Optional, Tuple
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


def parse_stock_page(html: str) -> Tuple:
    """Parse single stock page to get price, pe, profit, code, name."""
    soup = BeautifulSoup(html, "html.parser")

    name = soup.find("span", {"class": "price-section__label"}).text.strip()

    code = soup.find("span", {"class": "price-section__category"}).text.strip()

    price_raw = soup.find("span", {"class": "price-section__current-value"}).text
    price = float(price_raw.replace(",", "")) * usd_rate

    tag_price_low = "snapshot__data-item snapshot__data-item--small"
    price_low_raw = soup.find_all("div", {"class": tag_price_low})[-1].text.split()[0]
    price_low = price_low_raw.replace(",", "")

    tag_price_high_list = (
        "snapshot__data-item snapshot__data-item--small snapshot__data-item--right"
    )
    price_high_raw = soup.find_all("div", {"class": tag_price_high_list})[
        -1
    ].text.split()[0]
    price_high = price_high_raw.replace(",", "")
    profit_ratio = 100 * (float(price_high) - float(price_low)) / float(price_low)

    pe_raw = soup.find_all("div", {"class": "snapshot__data-item"})[8].text.split()[0]
    pe = pe_raw.replace(",", "")

    return name, code[8:], price, profit_ratio, float(pe)


def prepare_out(data: List, item_name: str) -> List[Dict]:
    """Prepare data to be written. Sort and slice."""
    is_reverse = True
    if item_name == "price":
        item_i = 2
    elif item_name == "potential profit":
        item_i = 3
    elif item_name == "P_E":
        item_i = 4
        is_reverse = False
    else:
        item_i = 5
    data_sort = sorted(data, key=lambda x: x[item_i], reverse=is_reverse)
    return [
        {"code": stock_data[1], "name": stock_data[0], item_name: stock_data[item_i]}
        for stock_data in data_sort[:10]
    ]


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
        ncppp = executor.map(parse_stock_page, stock_htmls)
    data = []
    for y_growth, single_ncppp in zip(y_growths, ncppp):
        data.append(list(single_ncppp) + [float(y_growth[:-1])])

    filenames = ["price", "P_E", "growth", "potential profit"]
    all_data = [prepare_out(data, filename) for filename in filenames]

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
