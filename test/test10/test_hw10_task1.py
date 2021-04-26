"""TEST Homework 10.1."""

import pytest
from bs4 import BeautifulSoup

from hw.hw10.hw10_task1 import get_curr_usd_rate
from hw.hw10.hw10_task1 import get_href_from_main_page, get_year_growth_from_main_page
from hw.hw10.hw10_task1 import parse_stock_page


@pytest.fixture()
def snp_500_main_page1():
    # with open("test/test10/snp_500_main_page1.html") as f:
    with open("snp_500_main_page1.html") as f:
        text = f.read()
        return BeautifulSoup(text, "html.parser")


@pytest.fixture()
def snp_500_stock_page():
    # with open("test/test10/snp_500_stock_page_3M.html") as f:
    with open("snp_500_stock_page_3M.html") as f:
        return f.read()


@pytest.fixture()
def centrobank_exchange_page():
    # with open("test/test10/xmlfile.xml", "rb") as f:
    with open("xmlfile.xml", "rb") as f:
        text = f.read()
        return BeautifulSoup(text, "html.parser")


def test_get_href(snp_500_main_page1):
    soup = snp_500_main_page1
    first_href = get_href_from_main_page(soup)[0]
    assert first_href == ["3M", "https://markets.businessinsider.com/stocks/mmm-stock"]


def test_get_growth(snp_500_main_page1):
    soup = snp_500_main_page1
    first_growth = get_year_growth_from_main_page(soup)[0]
    assert first_growth == "39.83%"


def test_parse_stock(snp_500_stock_page):
    data = parse_stock_page(snp_500_stock_page, "50%")
    assert data.price == [{"name": "3M Co.", "code": "MMM", "price": 15155.4736}]


def test_get_usd_rate(centrobank_exchange_page):
    usd_rate = get_curr_usd_rate()
    assert usd_rate == 74.768
