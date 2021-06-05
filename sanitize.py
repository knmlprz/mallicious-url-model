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
        old = len(self.sanitized_url)
        self.sanitized_url = self.sanitized_url.translate(translate_dict)
        self.removed_chars = old - len(self.sanitized_url)

        
    def __split_url(self) -> None:
        """Splits given url to atomic parts"""
        __protocol, _, domain = self.original_url.split("/")[:3]

        # store only protocol and domain for further processing
        self.protocol = __protocol[:-1]  # remove semicolon at the end of prot
        # save subdomains in descending order
        self.subdomains = domain.split(".")[::-1]

    def __rm_punycode(self) -> None:
        """Filters punycode strings and counts it"""
        # Check which subdomain levels use punycodes
        using_pc = [idna.decode(sub) if "xn--" in sub else sub
                for sub in self.subdomains]
        self.sanitized_url = ".".join(using_pc[::-1])
        self.unicode_amount = [[True if ord(letter) > 127
            else False for letter in sub].count(True)
            for sub in using_pc]


        # TODO: list of similar characters from punycodes and ascii
        self.similar_unicode_amount = 0  # this is temporary 

    def get(self):
        return [self.sanitized_url, self.removed_chars, self.protocol, sum(self.unicode_amount), self.similar_unicode_amount]