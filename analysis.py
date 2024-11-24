import matplotlib.pyplot as plt
from scipy import stats

import shared


def main(source: str) -> None:
    """main function"""
    text = shared.parse_text(shared.get_source(source))
    to_plot: dict[str, list] = {"x": [], "y0": [], "y1": [], "y2": []}
    for count in range(25, 10**99, 5):
        dataf = shared.get_frequencies_df(text, count)
        chi2 = shared.chi_squared(dataf["actual_frequency"], dataf["zipf_frequency"])
        df_len = len(dataf)
        p_val = 1 - stats.chi2.cdf(chi2, df_len - 1)
        print(f"p-value = {p_val}; chi2 = {chi2}; df = {df_len - 1}")
        for axis, val in zip(to_plot, [count, p_val, df_len - 1, chi2]):
            to_plot[axis].append(val)
        if df_len < count:  # or p_val == 1
            # dataf.to_csv("out.csv")
            break

    plt.scatter(to_plot["x"], to_plot["y0"])
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
    # main(source="https://www.gutenberg.org/cache/epub/1129/pg1129.txt")
    histo_analysis("https://www.gutenberg.org/cache/epub/1129/pg1129.txt")
