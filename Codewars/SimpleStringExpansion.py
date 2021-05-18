"""
CodewarsSimple Simple Simple String Expansion
https://www.codewars.com/kata/5ae326342f8cbc72220000d2/train/python
"""


def string_expansion(s):
    r = ""
    for char in s:
        if char.isalpha():
            r += char
        elif char.isdigit():
            for alpha in s[s.index(alpha) :]:
                if alpha.isalpha():
                    r = "".join(int(char) * alpha)
    return r


print((string_expansion("3abc"), "aaabbbccc"))
print((string_expansion("3D2a5d2f"), "DDDaadddddff"))
print((string_expansion("0d0a0v0t0y"), ""))
print((string_expansion("3d332f2a"), "dddffaa"))
print((string_expansion("abcde"), "abcde"))
