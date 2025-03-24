💳 Credit Card Validator (credit.py)
This Python program checks if a credit card number is valid using Luhn’s Algorithm, and identifies the card type (AMEX, MASTERCARD, or VISA).

How It Works:
Prompts the user to enter a credit card number.

Applies Luhn’s Algorithm to determine if the card number is valid:

Multiply every other digit from the second-to-last by 2.

If the product is two digits, add the digits together.

Sum all the results and add the sum of the digits that weren’t multiplied.

If the total modulo 10 is 0, the number is valid.

Identifies the card type based on:

AMEX: 15 digits, starts with 34 or 37

MASTERCARD: 16 digits, starts with 51–55

VISA: 13 or 16 digits, starts with 4

Prints one of the following:

"AMEX"

"MASTERCARD"

"VISA"

"INVALID"
