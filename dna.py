import sys
import csv

# Check for correct number of args
if len(sys.argv) != 3:
    print("Usage: dna.py databases/file.csv sequences/file.txt")
    sys.exit(1)

database = sys.argv[1]
sequence = sys.argv[2]

# open txt file
s = open(sequence, 'r')
dna = s.read()

# read a csv file as list
csv_reader = open(database, 'r')
d = csv.reader(csv_reader)

# create a list of lists for each line in database
d_list = [line for line in d]

max_count = []

# For each STR, compute the longest run of consecutive repeats in the DNA sequence
for j in range(1, len(d_list[0])):

    STRs = d_list[0][j]
    STRs_count = 0
    index = dna.find(STRs)
    longest_count = 0

    while index <= len(dna) - 1:

        if dna[index: index + len(STRs)] == STRs:

            STRs_count += 1
            index += len(STRs)

            if STRs_count > longest_count:
                longest_count = STRs_count

        else:

            STRs_count = 0
            index += 1

    max_count.append(longest_count)

# For each row in the data, check if there is a match between max_count and a row in dataset.
# If so, print out the person's name
for i in range(1, len(d_list)):

    database_list = []

    for j in range(1, len(d_list[i])):

        database_list.append(int(d_list[i][j]))
        #print(database_list)

    if database_list == max_count:

        print(d_list[i][0])
        sys.exit()

print("No Match")
sys.exit()
