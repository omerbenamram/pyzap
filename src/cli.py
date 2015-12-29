from __future__ import absolute_import, unicode_literals, print_function, division
# -*- coding: utf-8 -*-
import click
import pyzap
from pyzap.categories import suggest_category
import pandas as pd

CATEGORY_FUZZ_THRESHOLD = 70


@click.command()
@click.option('-k', '-keyword', type=click.STRING, prompt=True)
@click.option('-c', '--category', help='Category to search')
@click.option('--csv', help='Use CSV instead of excel for output', is_flag=True)
@click.option('-o', '--output', type=click.Path(), help='Output path', required=True,
              prompt="Where should I save the results?")
@click.option('--max-pages', help='Max pages to scrape', type=click.INT)
def cli_main(keyword, category, output, csv, max_pages):
    # got surrogate escape
    if '?' in keyword:
        raise Exception("Could'nt read UNICODE arguments from argv in this shell :(\n"
                        "Use the python interface..")

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

    df = pd.DataFrame(pyzap.search(keyword=keyword, category=category, max_pages=max_pages)).transpose()
    if csv:
        df.to_csv(output)
        return

    df.to_excel(output)
    return
