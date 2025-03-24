🧬 DNA Profiling (dna.py)
This Python program identifies a person based on their DNA sequence by analyzing Short Tandem Repeats (STRs). It's based on the CS50 Problem Set 6 exercise and simulates a simplified version of real-world DNA profiling used in forensic science.

🧪 How It Works:
The program takes two command-line arguments:

A CSV file containing a list of individuals and the number of times specific STRs repeat in their DNA.

A text file containing the DNA sequence to analyze.

It then:

Reads the STR patterns from the CSV header.

Calculates the longest run of consecutive repeats of each STR in the provided DNA sequence.

Compares these counts against the profiles in the database.

If there’s an exact match to an individual in the database, it prints their name.

If no match is found, it prints "No match".

🔬 Example:
bash
Copy
Edit
$ python dna.py databases/large.csv sequences/5.txt
Lavender
This program demonstrates skills in string manipulation, file I/O, data structures, and pattern recognition, and is a great example of how basic bioinformatics techniques can be implemented in Python.

