"""This module is used to create clean URLs
Classes
-------
    UrlData
        Handles necessary info about inserted URL
"""
from typing import Tuple, List
import idna

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
    protocol: str
    unicode_amount: List[int]
    similar_unicode_amount: int
    subdomains: List[str]


    def __init__(self, url: str):
        """Constructs all the necessary data and cleans url to domain only
        
        Parameters
        ----------
        url : str
            url to be sanitized and analyzed
        """
        self.original_url = url 
        self.__split_url()
        self.__rm_punycode()
        self.__rm_chars()

    def __rm_chars(self):
        """Removes unwanted characters such as dashes and underscores"""
        translate_dict = {ord(c): None for c in "_-"}
        # TODO: removals and count those
        self.sanitized_url = self.sanitized_url.translate(translate_dict)

        
    def __split_url(self) -> None:
        """Splits given url to atomic parts"""
        __protocol, _, domain = self.original_url.split("/")[:3]

        # store only protocol and domain for further processing
        self.protocol = __protocol[:-1]  # remove semicolon at the end of prot
        self.domain = domain


    def __rm_unicode(self) -> None:
        """Filters punycode strings and counts it"""
        # Check if using Punycode
        if "xn--" in domain:
            layers = domain.split(".")
            if "xn--" in layers[-2:]:
                pass  # insert some penalty for using punycode

        # TODO: do some function that counts amount of unicode characters
        # after parsing punnycode
        self.unicode_amount = 0  # this is temporary 
        # TODO: list of similar characters from punycodes and ascii
        self.similar_unicode_amount = 0  # this is temporary 
