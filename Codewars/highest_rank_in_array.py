"""
    CodeWars - Highest Rank Number in an Array
    https://www.codewars.com/kata/5420fc9bb5b2c7fd57000004/train/python
    
    Complete the method which returns the number which is most frequent in the given input array.
    If there is a tie for most frequent number, return the largest number among them.
    Note: no empty arrays will be given.
"""


def highest_rank(arr: list[int]):
    # return max(arr, key=arr.count)
    return max(set(arr), key=arr.count)
    # arr_d = {i: arr.count(i) for i in arr}
    # return max(arr_d, key=)


# print(highest_rank([12, 10, 8, 12, 7, 6, 4, 10, 12]))  #  12
# print(highest_rank([12, 10, 8, 12, 7, 6, 4, 10, 10]))  #  10
# print(highest_rank([12, 10, 8, 8, 3, 3, 3, 3, 2, 4, 10, 12, 10]))  #  3
# print(highest_rank([10, 12, 8, 8, 12, 12, 8, 6, 4, 10, 10]))  #  12
print(
    highest_rank(
        [
            6,
            41,
            19,
            17,
            2,
            4,
            23,
            26,
            17,
            25,
            5,
            50,
            3,
            27,
            41,
            11,
            50,
            44,
            7,
            19,
            0,
            11,
            2,
        ]
    )
)  # 50)
