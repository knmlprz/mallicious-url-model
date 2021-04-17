"""This module is used to handle data from cert.pl
Data from cert can be obtained in different forms (raw, automaticly tagged)
"""
from utils import get_data
from datasets import dataset_top_100_poland
import pandas as pd
from metrics_calculators import get_best_lev_match


class Cert:
    """
    Handle data from cert

    Parameters
    ----------
    url : str
        Url to cert data in json format
    filename : str
        Name of file to save raw cert data

    """
    url: str
    filename: str

    def __init__(self, url: str, filename: str):
        self.url = url
        self.filename = filename

    def get_raw(self, force_download=False):
        """

        Parameters
        ----------
        force_download : bool
            Forces re-download of data

        Returns
        -------
        str
            Raw data from cert (format depends on url)
        """
        return get_data(url=self.url,
                        filename=self.filename,
                        force_download=force_download)

    def get_tagged_data(self, force_download=False) -> pd.DataFrame:
        """

        Parameters
        ----------
        force_download : bool


        Returns
        -------
        pd.Dataframe
            Dataframe with additional column (KnownDomainMatch)

        """
        dt = pd.read_json(self.get_raw(force_download=force_download))
        domains = pd.DataFrame(dt['DomainAddress'])
        domains.columns = ['Domain']
        # Remove .pl .com etc from domains by splitting
        # TODO: Find a better way to cut top-level domain
        known_domains = dataset_top_100_poland()['Domain'].str.split(".", n=1, expand=True)[0]

        dt["KnownDomainMatch"] = get_best_lev_match(domains)

        return dt

cert = Cert("https://hole.cert.pl/domains/domains.json", "Data/domains.json").get_tagged_data()
print(cert)