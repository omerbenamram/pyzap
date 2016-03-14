# coding=utf-8
import re
from typing import Union, Any, Sized

from pies.overrides import *

from pyzap.constants import BAD_CHARS, PRICE_RE


def _clean_string(info_string: str) -> str:
    return info_string.strip(BAD_CHARS)


def re_first_or_none(regex, string):
    match = re.search(regex, string)
    if match:
        return match.groups(0)[0]
    return None


def re_one_or_none(regex, string) -> Union[Any, None]:
    match = re.findall(regex, string)
    if match:
        one(match)
    return None


def one(collection: Sized) -> Any:
    if len(collection) > 1:
        raise RuntimeError('Too many objects given where only one is expected!')
    else:
        return collection[0]


def _handle_price(price_str):
    # handle price vs price range (2500 or '₪2500-3000')
    if not price_str:
        return None
    prices = PRICE_RE.findall(price_str)

    # numbers are formatted as 2,500 sometimes..
    prices = list(map(lambda x: int(x.replace(',', '')), prices))
    return min(prices), max(prices)
