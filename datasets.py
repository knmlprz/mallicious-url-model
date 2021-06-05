"""This module contains functions that return various datasets
and performs some basic cleaning on them.
"""


import pandas as pd

DATASET_TOP_100_POLSKA = "Data/top100-polska.csv"
DATASET_TOP_LEVEL_DOMAINS = "Data/top-level-domains.csv"
DATASET_SUB_DOMAINS = "Data/sub-domains.csv"


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


def dataset_domains() -> pd.DataFrame:
    """
    Dataframe with top-level domains

    Returns
    -------
    pd.Dataframe
        Dataframe with columns  FDomain  (.{domain})
                                Domain   ({domain})
    """
    top_level_domains = pd.read_csv(DATASET_TOP_LEVEL_DOMAINS, delimiter=',', index_col=False, header=None)
    top_level_domains = top_level_domains.join(top_level_domains[0].str.split(".", n=1, expand=True)[1])
    top_level_domains.columns = ["FDomain", "Domain"]
    return top_level_domains


def dataset_subdomains() -> pd.DataFrame:
    """
    Dataframe with domains and their subdomains.

    Returns
    -------
    pd.Dataframe
        Dataframe with columns  FDomain (.{subdomain}.{domain})
                                Subdomain ({subdomain})
                                Domain ({domain})


    """
    subdomains = pd.read_csv(DATASET_SUB_DOMAINS, index_col=False, header=None)
    subdomains = subdomains.join(subdomains[0].str.split(".", n=2, expand=True)[[1, 2]])
    subdomains.columns = ["FDomain", "Subdomain", "Domain"]
    return subdomains
