import re


def main():

    text = input("Text: ")

    letters = 0
    words = 0
    wordsW = 0
    sentences = 0

    # loop through the input text and count the letters
    for i in text:
        if i.isalpha() == True:
            letters += 1

    # using regex (findall())
    # to count words in string
    words = len(re.findall(r'\w+', text))

    # count words with ' in them like you're, I've
    wordsW = len(re.findall(r"\w+'\w+", text))

    c = {'.', '!', '?'}

    # loop through the input text and check if the (./?/!) condition applies
    for i in text:
        if (i in c):
            sentences += 1

    # L is the average number of letters per 100 words in the text,
    L = letters / (words - wordsW) * 100

    # S is the average number of sentences per 100 words in the text.
    S = sentences / (words - wordsW) * 100

    # Coleman-Liau index formula
    index = round(0.0588 * L - 0.296 * S - 15.8)

    # check if the index is higher or equal to 16 and print the grade
    if (index >= 16):

        print("Grade 16+")

    elif (index < 1):

        print("Before Grade 1")

    else:

        print("Grade", index)


main()