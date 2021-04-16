"""This module is used to handle data from cert.pl
Data from cert can be obtained in different forms (raw, automaticly tagged)
"""
from utils import get_data
from datasets import dataset_top_100_poland
import pandas as pd


class Cert:
    """
    Handle data from cert

    Parameters
    ----------
    url : str
        Url to cert data in TSV format
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

    def get_tagged_data(self, force_download=False):
        dt = pd.read_json(self.get_raw(force_download=force_download))
        domains = dt['DomainAddress']
        # Remove .pl .com etc from domains by splitting
        known_domains = dataset_top_100_poland()['Domain'].str.split(".", n=1, expand=True)[0]

        dt["KnownDomainMatch"] = ""

        known_domains = known_domains.sort_values(key=lambda x: x.str.len())

        for domain in domains:
            for known_domain in known_domains:
                if known_domain in domain:
                    dt.loc[dt['DomainAddress'] == domain, 'KnownDomainMatch'] = known_domain

        return dt
