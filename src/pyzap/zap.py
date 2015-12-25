import itertools
import re
import sys

import logbook
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

logger = logbook.Logger()
logger.handlers.append(logbook.StreamHandler(sys.stdout))

PRICE_RE = re.compile('[\d,]+', re.UNICODE)
BASE_URL = 'http://www.zap.co.il/models.aspx'
WORDS_RE = re.compile('\w+', re.UNICODE)
BAD_CHARS = ', :<>'


def _handle_price(price_str):
    # handle price vs price range (2500 or '₪2500-3000')
    if not price_str:
        return None
    prices = PRICE_RE.findall(price_str)

    prices = list(map(lambda x: int(x.replace(',', '')), prices))
    return min(prices), max(prices)


def _clean_string(info_string):
    return info_string.strip(BAD_CHARS)


def products_from_page(soup):
    results = soup.find_all(attrs={'class': 'ProdInfo'})
    results_dict = {}
    for info in results:
        # extract some general stuff
        title = info.find(attrs={'class': 'ProdInfoTitle'}).a.text
        price_info, min_price, max_price = info.parent.find(attrs={'class': 'pricesTxt'}), None, None
        if price_info:
            min_price, max_price = _handle_price(price_info.text)

        # handle all the details!
        valid_strings = (x for x in (filter(lambda x: WORDS_RE.match(x), info.strings)))

        details = {}
        # Details are (arbitrarily..) ordered as
        # info 1: a, b, c, info2: a, b ...
        while True:
            try:
                s = next(valid_strings)
                if s.strip().endswith(':'):
                    flag = True
                    matching_info = []
                    while flag:
                        info_string = next(valid_strings)
                        if info_string.strip().endswith(','):
                            matching_info.append(info_string)
                        else:
                            flag = False

                    description = ','.join(map(_clean_string, matching_info))
                    details[s] = description
                else:
                    continue

            except StopIteration:
                break

        results_dict[title] = details
        results_dict[title]['min_price'] = min_price
        results_dict[title]['max_price'] = max_price

    return results_dict


def get_max_available_page_in_context(soup):
    pages = soup.find_all(attrs={'class': 'NumRow'})
    if pages:
        return int(max(list(filter(lambda x: re.match('\d+', x),
                                   itertools.chain.from_iterable([p.strings for p in pages]))), key=int))
    else:
        return 1


def search(keyword, category=None, max_pages=10):
    with requests.Session() as s:
        total_results = {}
        params = {'keyword': keyword}
        if category:
            params['sog'] = category

        base = requests.Request(method='get', url=BASE_URL, params=params)
        logger.debug('Search Params: {}'.format(base.params))
        for page in tqdm(range(1, max_pages + 1)):
            params['pageinfo'] = page
            response = s.send(base.prepare())
            response.raise_for_status()

            soup = BeautifulSoup(response.content, "lxml")

            total_results.update(products_from_page(soup))
            max_page = get_max_available_page_in_context(soup)

            if max_page <= page:
                logger.debug('Hit max pages at {}, breaking'.format(page))
                break

    return total_results
