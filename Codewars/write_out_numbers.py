# Codewars - Write out numbers
# https://www.codewars.com/kata/52724507b149fa120600031d/train/python


def number2words(n):
    """ works for numbers between 0 and 999999 """
    if not n:
        return "zero"  # 0 is zero

    vals = {
        "0": "",
        "1": "one",
        "2": "two",
        "3": "three",
        "4": "four",
        "5": "five",
        "6": "six",
        "7": "seven",
        "8": "eight",
        "9": "nine",
    }

    s = ""
    for i in str(n):
        s += vals[i] + " "
    return s

    # look at individual number val and position (index in reverse order might help)

    # return int("".join(str(n)[::-1]))


print(number2words(13))
print(number2words(123))

"""
ten
eleven
twelve
thir + teen
four + teen
fif + teen
six + teen
seven + teen
eight + teen
nine + teen
twenty-
thir + ty-
four + ty-
fif + ty-
six + ty-
seven + ty-
eight + y
nine + ty
one + hundred
one + thousand
"""
