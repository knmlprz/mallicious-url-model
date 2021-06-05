"""This module makes it easy to access all the data from APIs

Classes
-------
    PolandCERT
        NASK Polish CERT database API

    PhishTank
        PhishTank API

    OpenFish
        OpenFish API

    AA419
        Artists Against 419 API
"""

import pandas as pd
import requests


class PolandCERT(pd.DataFrame):
    """This class makes it easy to access
    the NASK CERT database with malicious domains.

    Parameters
    ----------
        CERT_url : str
            url address of the Polish NASK CERT database
    """

    def __init__(self, CERT_url: str):
        """Initializes pandas.DataFrame and loads all the
        records from the given URL

        Parameters
        ----------
            CERT_url : str
                url address of the Polish NASK CERT database
        """
        df = pd.read_json(CERT_url)
        super().__init__(df)
        self.rename(columns={"DomainAddress": "domain"},
                    inplace=True)


class PhishTank(pd.DataFrame):
    """This class makes it easy to access
    the PhishTank database with malicious domains.

    Parameters
    ----------
        PhishTank_url : str
            url address of the PhishTank API
    """

    def __init__(self, PhishTank_url: str):
        """Initializes pandas.DataFrame and loads all the
        records from the given URL

        Parameters
        ----------
            PhishTank_url : str
                url address of the PhishTank API
        """
        df = pd.read_json(PhishTank_url)
        super().__init__(df)
        self.rename(columns={"url": "domain"},
                    inplace=True)


class OpenFish(pd.DataFrame):
    """This class makes it easy to access
    the OpenFish database with malicious domains.

    Parameters
    ----------
        OpenFish_url : str
            url address of the OpenFish API
    """

    def __init__(self, OpenFish_url: str):
        """Initializes pandas.DataFrame and loads all the
        records from the given URL

        Parameters
        ----------
            OpenFish_url : str
                url address of the OpenFish API
        """
        df = pd.read_table(OpenFish_url,
                           names=["domain"])
        super().__init__(df)


class AA419(pd.DataFrame):
    """This class makes it easy to access
    the Artists Against 419 database with malicious domains.

    Parameters
    ----------
        aa419_url : str
            Url address of the OpenFish API
        aa419_api_key : str
            API key of the Artists Against 419 dataset
    """

    def __init__(self, aa419_url: str, aa419_api_key: str):
        """Initializes pandas.DataFrame and loads first 500
        records from the given URL

        Parameters
        ----------
            aa419_url : str
                Url address of the Artists Against 419 API
            aa419_api_key : str
                API key of the Artists Against 419 dataset
        """
        df = self._get_page(aa419_url, aa419_api_key, 0)
        super().__init__(df)
        self.url = aa419_url
        self.api_key = aa419_api_key
        self.rename(columns={"Url": "domain"},
                    inplace=True)

    @staticmethod
    def _get_page(aa419_url: str,
                  aa419_api_key: str,
                  page_num: int,
                  page_size=500
                  ) -> pd.DataFrame:
        """Creates API request and decodes it into Pandas.DataFrame

        Parameters
        ----------
            aa419_url : str
                Url address of the Artists Against 419 API
            aa419_api_key : str
                API key of the Artists Against 419 dataset
            page_num : int
                Page number of fake sites in the database, starting at page 0
            page_size : int
                Number of fake sites on the page
        """
        request_url = aa419_url + f"{page_num}/{page_size}"
        r = requests.get(
            request_url,
            headers={"Auth-API-Id": aa419_api_key}
        ).json()
        return pd.DataFrame.from_dict(r)

    def get_all(self,
                page_limit=None,
                start_page=0
                ) -> pd.DataFrame:
        """Creates a set of API requests and concatenates
        them into the single Pandas.DataFrame

        Parameters
        ----------
            page_limit : int
                Number of pages to download
            start_page : int
                The number of page to start from

        Returns
        -------
            df : Pandas.DataFrame
                resulting DataFrame
        """
        df = pd.DataFrame()
        page = start_page
        while True:
            try:
                # TODO: implement multithreading
                new_df = self._get_page(self.url,
                                        self.api_key,
                                        page)
            except ValueError:
                break
            else:
                df = pd.concat([df, new_df], ignore_index=True)
            page += 1
            if page_limit and page >= page_limit:
                break
        df.rename(columns={"Url": "domain"},
                  inplace=True)
        return df
