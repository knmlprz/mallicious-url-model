"""This module is used to create clean URLs
Classes
-------
    UrlData
        Handles necessary info about inserted URL
"""
from typing import Tuple

@dataclass
class UrlData:
    """This dataclass contains all of the URL data

    Parameters
    ----------
        url : str
            Whole url (including, but not necessarily) http(s):// and everything
            after TLD
    """
    sanitized_url: str
    original_url: str
    removed_chars: int
    domain: str
    protocol: str
    unicode_amount: int
    similar_unicode_amount: int
    def __split_url(self) -> None:
        """Splits given url to atomic parts"""
        __protocol, _, domain = self.original_url.split("/")[:3]

        # store only protocol and domain for further processing
        self.protocol = __protocol[:-1]  # remove semicolon at the end of prot
        self.domain = domain

