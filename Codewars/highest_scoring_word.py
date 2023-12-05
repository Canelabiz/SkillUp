# [Training on Highest Scoring Word | Codewars](https://www.codewars.com/kata/57eb8fcdf670e99d9b000272/train/python)

from string import ascii_lowercase

table = {k: v for v, k in enumerate(ascii_lowercase, 1)}


def high(x):
    # SOL 1
    # word_points = {}
    # for word in x.split():
    #     points = 0
    #     for char in word.lower():
    #         if char.isalpha():
    #             points += table[char]
    #     word_points[word] = points
    # return max(word_points, key=word_points.get)

    # SOL 2
    # word_points = {}
    # for word in x.split():
    #     word_points[word] = sum(table[char] for char in word.lower() if char.isalpha())
    # return max(word_points, key=word_points.get)

    # SOL 3
    word_points = {
        word: sum(table[char] for char in word.lower() if char.isalpha())
        for word in x.split()
    }
    return max(word_points, key=word_points.get)


print(high("man i need a taxi up to ubud"))  # 'taxi'
print(high("what time are we climbing up the volcano"))  # 'volcano'
print(high("take me to semynak"))  # 'semynak'
print(high("aa b"))  # 'aa'
print(high("b aa"))  # 'b'
print(high("bb d"))  # 'bb'
print(high("d bb"))  # 'd'
print(high("aaa b"))  # "aaa"
