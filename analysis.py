"""
this is primarily for me, to create charts and stuff
i don't particullary care about code quality here
"""

import matplotlib.lines as mlines
import matplotlib.pyplot as plt
from scipy import stats

import shared


def main(source: str) -> None:
    """main function"""
    text = shared.parse_text(shared.get_source(source))
    to_plot: dict[str, list] = {"x": [], "y0": [], "y1": [], "y2": [], "y3": []}
    for count in range(25, 10**99, 5):
        dataf = shared.get_frequencies_df(text, count)
        chi2 = shared.chi_squared(dataf["actual_frequency"], dataf["zipf_frequency"])
        df_len = len(dataf)
        p_val = 1 - stats.chi2.cdf(chi2, df_len - 1)
        print(f"p-value = {p_val}; chi2 = {chi2}; df = {df_len - 1}")
        for axis, val in zip(
            to_plot, [count, p_val, df_len - 1, chi2, min(dataf["actual_frequency"])]
        ):
            to_plot[axis].append(val)
        if df_len < count or p_val == 1:  #
            # dataf.to_csv("out.csv")
            break
    _, ax1 = plt.subplots()

    # ax1.scatter(to_plot["x"], to_plot["y0"])
    # # plt.scatter(to_plot["x"], to_plot["y2"])
    # plt.title("P-Value vs Number of Words Considered in Frequency")
    # plt.xlabel("Number of Words Considered in Frequency")
    # plt.ylabel("P-Value")

    ax1.scatter(to_plot["x"], to_plot["y0"], c="tab:blue")
    ax1.set_ylabel("P-Value", color="tab:blue")

    # ax1.set_xlabel("words considered in frequency")

    # ax2 = ax1.twinx()
    # ax2.scatter(to_plot["x"], to_plot["y2"], c="tab:orange")
    # ax2.set_ylabel("Chi-Squared", color="tab:orange")
    # plt.title("P-Value and Chi-Squared vs Number of Words Considered in Frequency")

    ax2 = ax1.twinx()
    ax2.scatter(to_plot["x"], to_plot["y3"], c="tab:orange")
    ax2.set_ylabel("Frequency of Least Common Word", color="tab:orange")
    plt.title(
        "P-Value and Frequency of Least Common Word \n vs Number of Words Considered in Frequency"
    )
    line = ax1.add_line(
        mlines.Line2D(
            [0, len(dataf)], [0.05, 0.05], color="tab:red", transform=ax1.transAxes
        )
    )
    line.set_label("alpha")

    plt.show()


def histo_analysis(source: str) -> None:
    """main function"""
    text = shared.parse_text(shared.get_source(source))
    dataf = shared.get_frequencies_df(text)
    dataf.to_csv("macbeth_every_word.csv", index=False)
    axes = dataf.iloc[:30].plot(
        kind="bar",
        x="word",
        y=["actual_frequency", "zipf_frequency"],
        title="Word Frequency Analysis",
        ylabel="Frequency",
        rot=45,
    )

    axes.plot()
    plt.show()


if __name__ == "__main__":
    main(source="https://www.gutenberg.org/cache/epub/1129/pg1129.txt")
    # https://www.gutenberg.org/cache/epub/11/pg11.txt
    # main("https://www.gutenberg.org/cache/epub/11/pg11.txt")
