""" CodeWars - Sort the odd
https://www.codewars.com/kata/578aa45ee9fd15ff4600090d/train/python
"""


def odd(i):
    if i % 2 != 0:
        return i


def sort_array(source_array):
    # return [j if j % 2 == 0 else sorted(source_array)[i] for i, j in enumerate(source_array)]
    # return [j if j % 2 == 0 else sorted(source_array)[i] for i, j in enumerate(source_array)]
    stuff = []
    for i in source_array:
        stuff.append(odd(i))

    return stuff
    # return sorted(source_array, key=odd)

    # oddsorted = [x for x in sorted(source_array, key=odd) if x % 2 != 0]
    # print(oddsorted)
    # sol = []
    # for i in source_array:
    #     for j in oddsorted:
    #         if i % 2 == 0:
    #             sol.append(i)
    #         else:
    #             sol.append(j)
    # return sol


print(sort_array([5, 3, 2, 8, 1, 4]), [1, 3, 2, 8, 5, 4])
print(sort_array([5, 3, 1, 8, 0]), [1, 3, 5, 8, 0])
print(sort_array([]), [])
