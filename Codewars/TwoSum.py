"""
CodeWars - Two Sum
https://www.codewars.com/kata/52c31f8e6605bcc646000082/train/python
"""


def two_sum(numbers, target):
    for i in numbers:
        for j in range(numbers.index(i+1), len(numbers)):
            if i + j == target:
                return sorted([numbers.index(i), numbers.index(j)])


print(two_sum([1, 2, 3], 4))
print(two_sum([1234, 5678, 9012], 14690))
print(two_sum([2, 2, 3], 4))
