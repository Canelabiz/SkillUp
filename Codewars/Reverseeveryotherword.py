""" Codewars - Reverse every other word in the string
    https://www.codewars.com/kata/58d76854024c72c3e20000de/train/python """

""" Reverse every other word in a given string, then return the string.
Throw away any leading or trailing whitespace,
while ensuring there is exactly one space between each word.
Punctuation marks should be treated as if they are a part of the word in this kata. """


def reverse_alternate(string):
    return " ".join(
        i if string.split().index(i) % 2 == 0 else i[::-1] for i in string.split()
    )


print(reverse_alternate("Did it work?"))  # "Did ti work?"
print(
    reverse_alternate("I really hope it works this time...")
)  # "I yllaer hope ti works siht time..."
print(
    reverse_alternate("Reverse this string, please!")
)  # "Reverse siht string, !esaelp"
print(reverse_alternate("Have a beer"))  # "Have a beer"
print(reverse_alternate(""))  # ""

