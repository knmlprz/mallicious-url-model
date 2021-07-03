"""This module is used to calculate Shannon entropy of objects"""
import math
import numpy as np
from typing import Optional

# Propability of letter occuring in dataset
# for more info check '/Notebooks/Entropy.ipynb'
prop_of_letters = {'g': 0.017823195816706855,
                   'u': 0.019656863921083692,
                   'i': 0.04282234162349053,
                   'd': 0.02362298601231347,
                   'w': 0.06868367734904952,
                   'n': 0.04192416654368707,
                   'o': 0.05917547697301064,
                   's': 0.04087732549559563,
                   'p': 0.047038663571700494,
                   'a': 0.04921073758433189,
                   't': 0.07547396818911765,
                   'e': 0.05859317164000978,
                   'm': 0.03821830076858004,
                   'r': 0.03626613607334285,
                   '6': 0.005261345563926245,
                   '9': 0.004489300290958807,
                   '.': 0.06449691896747548,
                   '1': 0.0074827325750036165,
                   '2': 0.007503935952713802,
                   '0': 0.006426077392086318,
                   '8': 0.00587551654457156,
                   '/': 0.05952224307019093,
                   'b': 0.018622381413143332,
                   'c': 0.049838478726711724,
                   'z': 0.0043048914859593656,
                   '3': 0.0066693710060409025,
                   'h': 0.033948061659907026,
                   'f': 0.014128719284484144,
                   'l': 0.03218672736406151,
                   '7': 0.004617732178803359,
                   '%': 0.0009838367257526048,
                   '5': 0.0058310500324593425,
                   '4': 0.006094335402540674,
                   'j': 0.0035587749148775255,
                   'y': 0.0096172463185484,
                   'x': 0.006756123111415147,
                   "'": 0.00032895525990373425,
                   'v': 0.007133179748181417,
                   '\\': 0.0007063753831450352,
                   '&': 0.0015393652217594634,
                   ';': 0.0008533450812162063,
                   'q': 0.0019404119658778284,
                   'k': 0.009749313071143269,
                   '(': 1.0662269934264683e-05,
                   ')': 1.0783432092608599e-05,
                   ',': 9.123510523296938e-05,
                   '#': 1.853781022661928e-05,
                   '[': 2.7867296419100876e-06,
                   ']': 2.7867296419100876e-06,
                   '*': 4.361837700381007e-06,
                   '$': 5.088810650444507e-06}


# Filter all characters present in dictionary
# cleaner = re.compile(r"""[^a-z0-9/;,.\'\[\]@&%1#$*()\\]+""")

def entropy(x: np.array, p: Optional[dict] = None):
    """
    Calculates Shannon [1]_ entropy of x, where x is a vector of symbols (for example list of letters) and p is a dict
    with probability of each symbol occurring. By default `p` (if `p` is `None`) is calculated based on x, as in [3]_,
    otherwise `p` is used as probability [2]_.

    Parameters
    ----------
    x : numpy.array
        Vector of symbols.
    p : dict
        Dict with probability of each symbol occurring.

    Returns
    -------
    float
        Entropy of x.

    Examples
    --------
    Fair coin toss:
    >>> print(entropy(np.array([l for l in "12"])))
    1

    References
    __________
    [1] Shannon, “A Mathematical Theory of Communication.”

    [2] Kaplan, "Shannon Entropy.", http://bearcave.com/misl/misl_tech/wavelets/compression/shannon.html

    [3] fmark, "How do I compute approximate entropy of a string",
        https://stackoverflow.com/questions/2979174/how-do-i-compute-the-approximate-entropy-of-a-bit-string
    """

    if p is None:
        p = [float(np.sum(x == c)) / len(x) for c in dict.fromkeys(x)]

    return - sum([prob * math.log(prob) / math.log(2.0) for prob in p])

# print(entropy(np.array([l for l in "1212121222222111111"])))
