"""This module is used to handle data rom cert.pl
Data from cert can be obtained in different forms (raw, tagged)
"""
from utils import get_data


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
