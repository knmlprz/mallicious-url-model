import requests
import os.path


def get_data(url, filename, force_download=False):
    """
    Download data from url save it to file as text.

    Parameters
    ----------
    url : str
        Url to dataset.
    force_download : bool
        If True data is downloaded from url, otherwise loaded from file
    filename : str
        Name of file to load/save

    Returns
    -------
    str
        Text response (json format)
    """

    if force_download or not os.path.exists(filename):
        # Download file and save it
        text_response = requests.get(url).text
        with open(filename, 'w') as f:
            f.write(text_response)
    else:
        # Check if file exists, load if so
        with open(filename, 'r') as f:
            text_response = f.read()

    return text_response
