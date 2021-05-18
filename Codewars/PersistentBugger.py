# CodeWars Persistent Bugger.


def persistence(n):
    l = []
    for x in [l += str(n)]:
        

    pass





'''
from math import prod


def persistence(n):
    c = 0
    while len(str(n)) > 1:
        # n = math.prod(map(int, str(n))) # Python 3.8
        n = prod(map(int, str(n))) # Python 3.8
        c += 1
    return c
    # return n if len(str(n)) == 1 else persistence(math.prod(map(int, str(n))))
'''

print(persistence(39))
print(persistence(4))
print(persistence(25))
print(persistence(999))
