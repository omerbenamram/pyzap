from __future__ import absolute_import, unicode_literals, print_function, division
# -*- coding: utf-8 -*-

import requests
import re
from bs4 import BeautifulSoup
from functools import partial
from googleapiclient.discovery import build

from pyzap.categories import ZapCategory

computers_categories = r'http://www.zap.co.il/cat.aspx?cat=comp'
electric_categories = r'http://www.zap.co.il/cat.aspx?cat=electric'

with open('apikey.txt') as apikey:
    GOOGLE_TRANSLATE_APIKEY = apikey.read()

TRANSLATOR = build('translate', 'v2', developerKey=GOOGLE_TRANSLATE_APIKEY)


def translate_from_gtranslate(query, source_lang, target_lang, translator):
    translations = (translator.translations().list(
        source=source_lang,
        target=target_lang,
        q=query
    ).execute())
    if translations:
        return list(zip(query, [list(x.values())[0] for x in translations['translations']]))


he_to_en = partial(translate_from_gtranslate, target_lang='en', source_lang='he', translator=TRANSLATOR)
CAT_RE = re.compile("/models\.aspx\?sog=([\w-]+)")


def categories_from_category_page(page, verbose=True):
    r = requests.get(page)
    soup = BeautifulSoup(r.content, 'lxml')

    results = {}
    for cb in soup.find_all(attrs={'class': 'CategoriesListBlock'}):
        key = he_to_en([cb.h2.text])[0][1]

        categories = []
        for x in cb.find_all('a', href=CAT_RE):
            he_description, en_description = x.text, he_to_en([x.text])[0][1]
            categories.append(ZapCategory(CAT_RE.findall(x.get('href'))[0], he_description, en_description))

        results[key] = categories

    if verbose:
        for k, l in results.items():
            print('-----------{}---------'.format(k))
            for a in l:
                print('{}={}'.format(a.english_description.replace(' ', ''), a))

    return results
