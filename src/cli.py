from __future__ import absolute_import, unicode_literals, print_function, division
# -*- coding: utf-8 -*-
import click
import logbook
import sys

import pyzap
from pyzap.categories import suggest_category
import pandas as pd

CATEGORY_FUZZ_THRESHOLD = 70

if hasattr(sys, '_called_from_test'):
    # called from within a test run
    logger = logbook.Logger(level=logbook.DEBUG)
else:
    logger = logbook.Logger(level=logbook.INFO)


@click.command()
@click.argument('keyword', nargs=1, type=click.STRING)
@click.option('-c', '--category', help='Category to search')
@click.option('--csv', help='Use CSV instead of excel for output')
@click.option('-o', '--output', type=click.Path(), help='Output path', required=True)
def cli_main(keyword, category, output, csv):
    if category:
        while True:
            categories = suggest_category(category)
            if categories:
                match = categories[0]
                if match[1] > CATEGORY_FUZZ_THRESHOLD:
                    category = match[0]
                    break

            category = click.prompt("Couldn't match any known category.. Closest matches:\n"
                                    "{}\n"
                                    "Re enter category please".format([x[0] for x in categories]))

    df = pd.DataFrame(pyzap.search(keyword=keyword, category=category)).transpose()
    if csv:
        df.to_csv(output)
        return

    df.to_excel(output)
    return
