"""
main file for this project

USAGE:
    python3 main.py "https://www.gutenberg.org/cache/epub/84/pg84.txt" # frankenstien
    python3 main.py "https://www.gutenberg.org/cache/epub/1129/pg1129.txt" -c 100 # macbeth w/ 100 most common words
    python3 main.py "https://www.gutenberg.org/cache/epub/120/pg120.txt" -c 100 -o "treasure-island.csv" # treasure island w/ 100 most common words and exports to csv
    python3 main.py "https://www.gutenberg.org/cache/epub/11/pg11.txt" # alice in wonderland]

see README.md
johan cho 2024-11-21
"""

import argparse

# import statistics
from scipy import stats

import shared


def main(_source: str, word_count: int | None = None, outfile: str = "") -> None:
    """main function but returns a value instead of printing

    args:
        - _source (str): filepath or url to a `.txt` file to process
        - word_count (int | None): words to consider in most common
        - outfile: (str) default None
    returns:
        - None
    """
    text = shared.parse_text(shared.get_source(_source))
    dataframe = shared.get_frequencies_df(text, word_count)
    if outfile:
        dataframe.to_csv(outfile)
    chi2 = shared.chi_squared(
        dataframe["actual_frequency"], dataframe["zipf_frequency"]
    )
    df_ = len(dataframe) - 1
    print(f"p-value = {1 - stats.chi2.cdf(chi2, df_)}; chi2 = {chi2}; df = {df_}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="""input: text file, typically a novel.
        prints out the resultant zipf distribution and chi-squared score
    """
    )
    parser.add_argument(
        "--count",
        "-c",
        type=int,
        default=None,
        help="how many words to consider, defaults to every word",
    )

    parser.add_argument(
        "--outfile", "--out", "-o", default="", help="where to export a csv to"
    )

    group = parser.add_mutually_exclusive_group()

    group.add_argument(
        "--source", "-s", help="filepath or url to a `.txt` file to process"
    )
    group.add_argument("static_source", nargs="?", default="")
    results = parser.parse_args()
    if not (source := results.source or results.static_source):
        raise ValueError("you must provide a source")
    main(source, results.count, results.outfile)
