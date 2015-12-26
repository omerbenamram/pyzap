from __future__ import absolute_import, unicode_literals, print_function, division
# -*- coding: utf-8 -*-
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


def test_gets_resutls(products_page):
    page_results = products_from_page(products_page)
    assert len(page_results) > 0


def test_categories_extracted_correctly(products_page):
    page_results = products_from_page(products_page)
    # when columns are extracted badly - we get out of split results such as dates as columns.

    title, details = next(iter(page_results.items()))
    assert set(details.keys()) == \
           {'יצרן', 'גודל מסך', 'רזולוציה מקסימלית', 'סוג פאנל', 'זמן תגובה', 'סוג המסך', 'רמקולים', '\u200fPivot',
            'תלת מימד', 'חיבורים',
            'תאריך כניסה לזאפ', 'min_price', 'max_price'}

    for title, details in page_results.items():
        for k, v in details.items():
            assert not DATE_REGEX.match(k)
