# Codewars - Count letters in string
# https://www.codewars.com/kata/5808ff71c7cfa1c6aa00006d/train/python


def letter_count(s):
    return {x: s.count(x) for x in sorted(set(s))}

    # for x in sorted(set(s)):
    #         print(x, s.count(x))


print(letter_count("codewars"))
print(letter_count("activity"))
print(letter_count("arithmetics"))
print(letter_count("traveller"))
print(letter_count("daydreamer"))