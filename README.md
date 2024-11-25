# MATH4581 Final

## problem statement

See how well Zipf’s Law corresponds to a novel. Choose a novel and get the count for the 100 (at least) most common words, then get the probability of each to see if it follow’s Zipf’s Law. Use the χ2 goodness of fit test to see how well it fits.

Note: Use a variation (called the Zipf-Mandelbrot distribution), which is:

```python
(1 / (K + 2.7)) / sum(1 / (i + 2.7) for i in range(1, N + 1)) # (your N will be 20).
```

## usage

```bash
python3 main.py <url> -c <words_to_consider> -o <outfile>
```

this python script takes a url or file as an argument. the argument should point to a plaintext `.txt` file.

## books

```bash
python3 main.py "https://www.gutenberg.org/cache/epub/84/pg84.txt" # frankenstien
python3 main.py "https://www.gutenberg.org/cache/epub/1129/pg1129.txt" -c 100 # macbeth w/ 100 most common words
python3 main.py "https://www.gutenberg.org/cache/epub/120/pg120.txt" -c 100 -o "treasure-island.csv" # treasure island w/ 100 most common words and exports to csv
python3 main.py "https://www.gutenberg.org/cache/epub/11/pg11.txt" # alice in wonderland
```
