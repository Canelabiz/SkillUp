"""
CodeComabat - The Vowel Code
https://www.codewars.com/kata/53697be005f803751e0015aa/train/python

Step 1: Create a function called encode() to replace all the lowercase vowels in a given string with numbers according to the following pattern:
For example, encode("hello") would return "h2ll4".

Step 2: Now create a function called decode() to turn the numbers back into vowels according to the same pattern shown above.
For example, decode("h3 th2r2") would return "hi there".
"""
vowels = ["a", "e", "i", "o", "u"]

# dict comprehension
{v: n for n, v in enumerate(["a", "e", "i", "o", "u"], 1)}
{n: v for n, v in enumerate(["a", "e", "i", "o", "u"], 1)}

{v: n for n, v in enumerate(vowels, 1)}
{n: v for n, v in enumerate(vowels, 1)}

vowels = ["a", "e", "i", "o", "u"]

# list comprehension
[str(i) for i in range(1, 5 + 1)]  # create a list of string-casted integers


def encode(st):
    return "".join(
        char
        if char not in vowels
        else str({v: n for n, v in enumerate(vowels, 1)}[char])
        for char in st
    )


def decode(st):
    return "".join(
        char
        if char not in [str(i) for i in range(1, 5 + 1)]
        else {n: v for n, v in enumerate(vowels, 1)}[int(char)]
        for char in st
    )


print(encode("hello"), "h2ll4")
print(encode("How are you today?"), "H4w 1r2 y45 t4d1y?")
print(encode("This is an encoding test."), "Th3s 3s 1n 2nc4d3ng t2st.")
print(decode("h2ll4"), "hello")
print(decode("2"))
