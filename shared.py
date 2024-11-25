"""
for sharing across main.py and analysis.py
"""

import re
import typing as t
import urllib.request as requests
from collections import Counter

import pandas as pd


def get_frequencies_df(_text: str, word_count: int | None = None) -> pd.DataFrame:
    """returns a dataframe of frequencies and zipf predictions.

    args:
        - _text: text to process, sep by " "
        - word_count (int | None): words to consider in most common \n
    returns:
        - pd.Dataframe[
            "word" |
            "actual_probability" |
            "actual_frequency" |
            "zipf_probability" |
            "zipf_frequency"
        ]
    """
    # split_text = _text.split()
    words, counts = zip(*Counter(_text.split()).most_common(word_count))
    dataframe = pd.DataFrame({"word": words, "actual_frequency": counts})
    _total = dataframe["actual_frequency"].sum()
    # _total = len(split_text)
    dataframe["actual_probability"] = dataframe["actual_frequency"] / _total
    dataframe["zipf_probability"] = dataframe.index.to_series().apply(
        lambda x: zipf_pdf(x + 1, len(dataframe))
    )
    dataframe["zipf_frequency"] = dataframe["zipf_probability"] * _total
    return dataframe


def chi_squared(
    actual: t.Iterable[float | int], expected: t.Iterable[float | int]
) -> float:
    """returns the chi-squared score of two datasets

    args:
        - actual (Iterable[float | int]): actual dataset
        - expected (Iterable[float | int]): expected dataset\n
    returns:
        - float: the chi-squared score
    """
    return sum((a - e) ** 2 / e for a, e in zip(actual, expected))


def zipf_pdf(_k: int, _n: int, _a: float = 2.7) -> float:
    """returns the probablity P(X = k) for the Zipf-Mandelbrot distribution

    args:
        - _k (int): integer above 0, this is the rank of the object
        - _n (int): total length of the dataset
        - _a (float): 2.7 by default \n
    returns:
        - float: the probability
    """

    if not _k:
        raise ValueError("_k must be above 0 and int")
    return (1 / (_k + _a)) / sum(1 / (i + _a) for i in range(1, _n + 1))


# GET_SOURCE_CACHE: dict[str, str] = {}
# global GET_SOURCE_CACHE
# if cache and _source in GET_SOURCE_CACHE:
#     _source = GET_SOURCE_CACHE[_source]


def get_source(_source: str) -> str:
    """parses the source and returns the content. if url, it goes to `/tmp`

    args:
        - _source (str): filepath or url to a `.txt` file to process\n
    returns:
        - str: the raw contentget_source(_source)).sp
    """
    if _source.startswith("http"):
        _source, _ = requests.urlretrieve(_source)
    with open(_source, encoding="utf-8") as raw:
        return raw.read()


def parse_text(_text: str) -> str:
    """parses the source, cleaning it up

    - removes "”", "“", ",", "?", ".", "!", ";"
    - replaces newlines and "--" with " "
    - replaces excess spaces and tabs with " "
    - removes gutenburg library text (thanks tho!)

    args:
        - _text (str): filepath or url to a `.txt` file to process\n
    returns:
        - str: parsed source.
    """
    _text = re.sub(r"[”“,?.!;:)(—_—]", "", _text)
    for to_space in ["\n", "--"]:
        _text = _text.replace(to_space, " ")
    _text = re.sub(r"\s{2,}", " ", _text).lower()
    if "*** start of" in _text:
        _text = _text.split("*** start of")[1].split("***")[1]
    if "*** end of" in _text:
        _text = _text.split("*** end of")[0]
    return _text.strip()
