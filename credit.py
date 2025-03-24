import math


def main():

    card_number = get_userinput()
    digits = len(str(abs(card_number)))

    # find the first digit and first 2 digits
    first_digit = first_n_digits(card_number, 1)
    two_digits = first_n_digits(card_number, 2)

# if checksum is true -> check for card length and starting digits
    if (checksum(card_number) == 0):

        if ((first_digit == 4) and (digits == 13 or digits == 16)):

            print("VISA")

        elif ((two_digits == 34 or two_digits == 37) and digits == 15):

            print("AMEX")

        elif ((two_digits == 51 or two_digits == 52 or two_digits == 53 or two_digits == 54 or two_digits == 55) and digits == 16):

            print("MASTERCARD")

        else:

            print("INVALID")

    else:

        print("INVALID")


# get the user's input (card number)
def get_userinput():

    card_number = int(input("Number: \n"))
    digits = len(str(abs(card_number)))

    # find the total number of digits
    while (digits < 0):

        card_number = int(input("Number: \n"))

    return card_number


# find the n-th digit in a number
def first_n_digits(num, n):

    return num // 10 ** (int(math.log(num, 10)) - n + 1)


def checksum(card_number):

    digits = len(str(abs(card_number)))
    card_numberC = card_number / 10  # remove the last digit

    sumBD = 0  # sum between digits
    sumD = 0  # sum digits
    sumT = 0  # sum total

    # check algorithm when card_number has 14 or 16 digits
    if (digits == 16 or digits == 14):

        while(card_numberC > 0):

            lastdigit = card_numberC % 10  # find the last digit after removing a digit from the end of the card_number
            otherdigit = card_number % 10  # find the card_number's last digit
            doubledigit = lastdigit * 2  # multiply every other digit by 2

            if (doubledigit > 9):  # if after multiplying doubledigit is grather than 9, add up the digits

                sumBD += doubledigit / 10 + doubledigit % 10  # sum between digits  = digit before last + last digit

            else:

                sumBD += doubledigit

            card_numberC /= 100  # remove 2 digits
            card_number /= 100   # remove 2 digits
            sumD += otherdigit
            sumT = sumD + sumBD  # sum total

        return (sumT % 10 == 0)

    # check algorithm when card_number has 15, 13 or less digits
    else:

        while (card_number > 0):

            lastdigit = card_numberC % 10  # find the last digit after removing a digit from the end of the card_number
            otherdigit = card_number % 10  # find the card_number's last digit
            doubledigit = lastdigit * 2  # multiply every other digit by 2

            if (doubledigit > 9):  # if after multiplying doubledigit is grather than 9, add up the digits

                sumBD += doubledigit / 10 + doubledigit % 10  # /sum between digits  = digit before last + last digit

            else:

                sumBD += doubledigit

            card_numberC /= 100  # remove 2 digits
            card_number /= 100   # remove 2 digits
            sumD += otherdigit

            sumT = sumD + sumBD  # total sum

        return (sumT % 10 == 0)  # if sum's last digit is 0, Luhn’s Algorithm = true


main()