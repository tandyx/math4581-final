# MATH4581 Final

## problem statement

See how well Zipf’s Law corresponds to a novel. Choose a novel and get the count for the 100 (at least) most common words, then get the probability of each to see if it follow’s Zipf’s Law. Use the χ2 goodness of fit test to see how well it fits.

Note: Use a variation (called the Zipf-Mandelbrot distribution), which is:

    ```py
    (1 / (K + 2.7)) / sum(1 / (i + 2.7) for i in range(1, N + 1)) # (your N will be 20).
    ```

## usage

    ```bash
    python3 main.py <url>
    ```

this python script takes a url or file as an argument. the argument should point to a plaintext `.txt` file.

## books

    ```bash
    python3 main.py "https://www.gutenberg.org/cache/epub/84/pg84.txt" # frankenstien
    python3 main.py "https://www.gutenberg.org/cache/epub/1129/pg1129.txt" # macbeth
    python3 main.py "https://www.gutenberg.org/cache/epub/120/pg120.txt" # treasure island
    python3 main.py "https://www.gutenberg.org/cache/epub/11/pg11.txt" # alice in wonderland
    ```

## questions for professor linde

1. I found the probability (frequency) of each word. We don't need that for chi-squared though right?
2. Shouldn't N be the number of words that you're testing, not 20?
3. Do I have to write a report? / What are you expecting in this submission?
4. I use a builtin library for getting word counts, is this alright?
5. Should I graph stuff and output the frequencies, etc.
6. when I calculate the frequencies, do I consider the sample set I chose (the largest 150) or the entire dataset?
