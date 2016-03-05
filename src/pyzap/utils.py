# coding=utf-8
import re
from typing import Union, Any, Sized


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


BAD_CHARS = ', :<>'