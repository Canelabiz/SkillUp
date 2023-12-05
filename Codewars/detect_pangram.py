# [Training on Detect Pangram | Codewars](https://www.codewars.com/kata/545cedaa9943f7fe7b000048/train/python)

from string import ascii_lowercase


def is_pangram(s):
    # matches = 0
    # matched = ""
    # for i in set(s.lower()):
    #     if i.isalpha() and i in ascii_lowercase:
    #         matches += 1
    #         matched += i
    # return matches == 26s

    return sum(1 for i in set(s.lower()) if i.isalpha() and i in ascii_lowercase) == 26


print(is_pangram("The quick, brown fox jumps over the lazy dog!"))  # True
print(is_pangram("1bcdefghijklmnopqrstuvwxyz"))  # False
