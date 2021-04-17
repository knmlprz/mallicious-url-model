"""This module contains functions that return various datasets
and performs some basic cleaning on them.
"""


import pandas as pd

DATASET_TOP_100_POLSKA = "Data/top100-polska.csv"


def dataset_top_100_poland(filename=DATASET_TOP_100_POLSKA) -> pd.DataFrame:
    """

    Parameters
    ----------
    filename : str
        Path to file to read

    Returns
    -------
    pd.Dataframe
        Dataframe with columns Type, Domain

    """
    dataset = pd.read_csv(filename, delimiter=',', index_col=0)
    return dataset
