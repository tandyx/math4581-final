"""
main file for this project
see README.md
johan cho 2024-11-21
"""

import argparse
import re
import urllib.request as requests
from collections import Counter


def main(_source: str) -> None:
    """main function

    args:
        - _source (str): filepath or url to a `.txt` file to process
    """
    text = parse_text(get_source(_source))
    counts = Counter(text.split()).most_common(150)
    total_count = sum(c for _, c in counts)
    probabilities = {word: cnt / total_count for word, cnt in counts}
    print(text)


def get_source(_source: str) -> str:
    """parses the source and returns the content. if url, it goes to `/tmp`

    args:
        - _source (str): filepath or url to a `.txt` file to process\n
    returns:
        - str: the raw content
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
    _text = re.sub(r"[”“,?.!;:]", "", _text)
    for to_space in ["\n", "--"]:
        _text = _text.replace(to_space, " ")
    _text = re.sub(r"\s{2,}", " ", _text).lower()
    if "*** start of" in _text:
        _text = _text.split("*** start of")[1].split("***")[1]
    if "*** end of" in _text:
        _text = _text.split("*** end of")[0]
    return _text.strip()


def zipf_pdf(_k: int, _n: int) -> float:
    """returns the probablity P(X = k) for the Zipf-Mandelbrot distribution

    args:
        - _k (int) integer above 0
        - _n (int)\n
    returns:
        - float: the probability
    """

    if not _k:
        raise ValueError("_k must be above 0 and int")
    return (1 / (_k + 2.7)) / sum(1 / (i + 2.7) for i in range(1, _n + 1))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="""input: text file, typically a novel.
        prints out the resultant zipf distribution and chi-squared score
    """
    )
    group = parser.add_mutually_exclusive_group()

    group.add_argument(
        "--source", "-s", help="filepath or url to a `.txt` file to process"
    )
    group.add_argument("static_source", nargs="?", default="")
    results = parser.parse_args()
    if not (
        source := results.source
        or results.static_source
        or "https://www.gutenberg.org/cache/epub/120/pg120.txt"
    ):
        raise ValueError("you must provide a source")
    main(_source=source)
