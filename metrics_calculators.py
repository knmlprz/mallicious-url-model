""" This module contains functions that calculate various metrics for two strings
"""
import numpy as np
import pandas as pd
import re
import ipaddress
from urllib3.util import parse_url


def parseurl(url):
    try:
        url = url.translate({'[': None, ']': None})
        url = parse_url(url)
        return url
    except Exception as e:
        return np.nan


def count_special_symbols(domain):
    counter = 0
    for char in domain:
        if char.isalpha() or char.isdigit():
            continue
        else:
            counter += 1
    return counter


def count_digits(domain):
    counter = 0
    for char in domain:
        if char.isdigit():
            counter += 1
    return counter


def count_digit_letter(domain):
    """Zlicza kombinacje litera cyfra"""
    res = re.findall("[A-Za-z][0-9]", domain)
    return len(res)


def count_sus(domain):
    res = re.findall("https|http|www", domain)
    return len(res)


def has_a(domain):
    """Sprawdza czy domain ma @"""
    res = re.findall("@", domain)
    return len(res)


def has_pref_or_suff(domain):
    """Sprawdza czy domain ma -"""
    res = re.findall("-", domain)
    return len(res)


def is_ipv4(string):
    try:
        ipaddress.IPv4Network(string)
        return True
    except ValueError:
        return False


def calculate_metrics(df_):
    ##### Schema
    schema = df_.schema
    schema = schema.fillna("n")
    schema = schema.replace(
        {"https": 1, "http": 0, "n": 0.5, 'none': 0.5, 'hhtp': 0, 'nttps': 1, "htpps": 1, "htps": 1, "htt": 0})
    schema = schema.astype('float64')

    #### Host
    host = df_.host
    host_len = host.apply(lambda x: len(x))  # Długość
    host_subdomains_count = host.apply(lambda x: x.count('.'))  # Ilość subdomen
    host_subdomains_mean_len = host.apply(lambda x: (len(x) - x.count('.')) / x.count('.'))  # Średnia długość domen
    host_digit = host.apply(lambda x: count_digits(x))  # Ilość cyfr
    host_nspecial = host.apply(lambda x: count_special_symbols(x) - x.count('.'))  # Ilość znaków specjalnych - kropki
    host_first_len = host.apply(lambda x: len(x.split('.')[0]))  # Długość pierwszej subdomeny
    host_digit_letter_count = host.apply(lambda x: count_digit_letter(x))  # Ilość kombinacji litera-cyfra
    host_has_a = host.apply(lambda x: has_a(x))  # Sprawdza czy host ma @
    host_pref_suf_number = host.apply(lambda x: has_pref_or_suff(x))  # Sprawdza czy ma -
    host_is_ipv4 = host.apply(lambda x: is_ipv4(x))  # Sprawdza czy host to adres ipv4s

    return np.array(
        [schema, host_len, host_subdomains_count, host_subdomains_mean_len, host_digit, host_nspecial, host_first_len,
         host_digit_letter_count, host_has_a, host_pref_suf_number, host_is_ipv4]).T


def transform(url):
    """Transforms """
    d = pd.DataFrame([url], columns = ['url'])
    d['parsed_url'] = d.url.apply(lambda x : parseurl(x))
    u = d.url.apply(lambda x : list(parseurl(x)))
    d['schema'] = u.apply(lambda x : x[0])
    d['auth'] = u.apply(lambda x : x[1])
    d['host'] = u.apply(lambda x : x[2])
    d['port'] = u.apply(lambda x : x[3])
    d['path'] = u.apply(lambda x : x[4])
    d['query'] = u.apply(lambda x : x[5])
    d['fragment'] = u.apply(lambda x : x[6])
    return d
