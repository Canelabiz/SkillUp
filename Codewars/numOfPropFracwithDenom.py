"""
CodeWars - Number of Proper Fractions with Denominator d
https://www.codewars.com/kata/55b7bb74a0256d4467000070/train/python
"""

from math import gcd


def proper_fractions(n):
    d = 0
    for i in range(1, n):
        if i % n == :
            d += 1
    return d


print(proper_fractions(1))
print(proper_fractions(2))
print(proper_fractions(5))
print(proper_fractions(15))
print(proper_fractions(25))
