""" CodeWars - Rot13 """

"""
ROT13 is a simple letter substitution cipher that replaces
a letter with the letter 13 letters after it in the alphabet.
ROT13 is an example of the Caesar cipher.
Create a function that takes a string and returns the string ciphered with Rot13.
If there are numbers or special characters included in the string,
they should be returned as they are.
Only letters from the latin/english alphabet should be shifted,
like in the original Rot13 "implementation".
"""

from string import ascii_lowercase, ascii_uppercase

alpha = ascii_lowercase + ascii_uppercase


def rot13(message):
    return "".join(message[pos + 13] for pos, c in enumerate(message) if c.isalpha())

    # [pos for pos, c in enumerate(message) if c == "t"]

    # "".join(chr(ord(c) + 13) if chr(ord(c) + 13).isalpha() else c for c in message)


print(rot13("test"), "grfg")
print(rot13("Test"), "Grfg")

# ord('A')
# chr(65)
