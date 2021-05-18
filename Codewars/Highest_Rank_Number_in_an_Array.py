""" Codewars - Highest Rank Number in an Array"""


def highest_rank(arr):
    # return max(set(arr), key=arr.count)
    # return max(arr, key=arr.count)
    # return max((arr.count(element), element) for element in set(arr))
    return max(arr.count(element) for element in set(arr))


print(highest_rank([12, 10, 8, 12, 7, 6, 4, 10, 12]), 12)
print(highest_rank([12, 10, 8, 12, 7, 6, 4, 10, 10]), 10)
print(highest_rank([12, 10, 8, 12, 7, 6, 4, 10, 12]), 12)
print(highest_rank([12, 10, 8, 12, 7, 6, 4, 10, 12, 10]), 12)
print(highest_rank([12, 10, 8, 8, 3, 3, 3, 3, 2, 4, 10, 12, 10]), 3)
