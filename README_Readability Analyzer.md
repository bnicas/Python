📚 Readability Analyzer (readability.py)
This Python program analyzes the readability of a given block of text using the Coleman-Liau index. It counts the number of letters, words, and sentences in the input and calculates the U.S. grade level needed to comprehend the text.

The program works as follows:

Prompts the user to enter a block of text.

Calculates:

L: Average number of letters per 100 words.

S: Average number of sentences per 100 words.

Applies the Coleman-Liau formula:
index = 0.0588 * L - 0.296 * S - 15.8

Rounds the index to the nearest whole number and outputs:

"Grade X" if 1 <= index < 16

"Grade 16+" if index >= 16

"Before Grade 1" if index < 1
