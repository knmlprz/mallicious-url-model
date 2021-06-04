""" This module contains functions that calculate various metrics for two strings
"""
import Levenshtein
import pandas as pd

from datasets import dataset_top_100_poland


def get_best_lev_match(domains: pd.DataFrame):
    """
    Calculates Levenshtein distance of given string to all domains in top-100 polish database and returns best domain
    and it's score.

    Returns
    -------

    """

    known_domains = pd.DataFrame(dataset_top_100_poland()['Domain'].str.split(".", n=1, expand=True)[0])
    known_domains.columns = ["Domain"]

    return domains.apply(lambda y: known_domains.iloc[
        known_domains.apply(lambda x: Levenshtein.jaro_winkler(y['Domain'], x['Domain'], 0.25), axis=1).idxmax()
    ], axis=1)
