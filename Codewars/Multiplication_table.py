""" Codewars - Multiplication table """
from timeit import timeit

setup = """
from random import randrange
size = randrange(1, 6)
"""

comp = """
def multiplication_table_lc(size):
    return [[a * b for b in range(1, size + 1)] for a in range(1, size + 1)]
"""

loop = """
def multiplication_table_fl(size):
    table = []
    for a in range(1, size + 1):
        row = []
        for b in range(1, size + 1):
            row.append(a * b)
        table.append(row)
    return table
"""

print(timeit(setup=setup, stmt=comp, number=100))
print(timeit(setup=setup, stmt=loop, number=100))
# print(multiplication_table_lc(n))
# print(multiplication_table_fl(n))
