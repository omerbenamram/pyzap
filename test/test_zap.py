import re

import pytest
import requests
from bs4 import BeautifulSoup

from pyzap.zap import products_from_page

SAMPLE_URL = 'http://www.zap.co.il/models.aspx?sog=c-monitor'
DATE_REGEX = re.compile('\d{1,2}/\d{1,4}')  # matches 01/2014


@pytest.fixture
def products_page():
    r = requests.get(SAMPLE_URL)
    return BeautifulSoup(r.content, 'lxml')


def test_categories_extracted_correctly(products_page):
    page_results = products_from_page(products_page)

    assert len(page_results) > 0

    # when columns are extracted badly - we get out of split results such as dates as columns.
    for title, details in page_results.items():
        for k, v in details.items():
            assert not DATE_REGEX.match(k)
