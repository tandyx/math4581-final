# MATH4581 Final

## problem statement

See how well Zipf’s Law corresponds to a novel. Choose a novel and get the count for the 100 (at least) most common words, then get the probability of each to see if it follow’s Zipf’s Law. Use the χ2 goodness of fit test to see how well it fits.

Note: Use a variation (called the Zipf-Mandelbrot distribution), which is:

    ```py
    (1 / (K + 2.7)) / sum(1 / (i + 2.7) for i in range(1, N + 1)) # (your N will be 20).
    ```

## usage

this python script takes a url or file as an argument. the argument should point to a plaintext `.txt` file. for now, this defaults into treasure island, which is a novel with an amazing intro and 2/3 of the way in it becomes unreadable.
