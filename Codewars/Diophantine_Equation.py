""" CodeWars - Diophantine Equation """
"""
x^2-4y^2 = (x-2y)*(x+2y) = 12 

(x-2y)(x+2y) = 12
x^2 -4y^2 = 12
x^2 -4y^2 - 12 = 0
4y^2 = x^2 - 12
2y = ((x^2 - 12)^1/2)
y = ((x^2 - 12)^1/2)/2


(a/d)a - (4/d)b = c/d
(x/d)x - (4/d)y = 12/d
(x/4)x - (4/4)y = 12/4
(x/4)x - (1)y = 3

(x) - (y) = c
4 - 1 = 3

x^2 - 4y^2 = 12
16 - 4 = 12
x = 4
y = 1
"""


def sol_equa(n):

    # A Pythagorean triple consists of three positive integers a, b, and c,
    # such that a^2 + b^2 = c^2.
    # Such a triple is commonly written (a, b, c), the best known example is (3, 4, 5).
    #

    return [x for x in range(1, min(4, n) + 1) if 4 % x == n % x == 0]

    # [
    #     [int(x), int((((x ** 2) - n) ** 0.5) / 2)]
    #     for x in range(100, 10000)
    #     if ((((x ** 2) - n) ** 0.5) / 2) >= 0 and ((((x ** 2) - n) ** 0.5) / 2) % 2 == 0
    # ]


print(sol_equa(12))
print(sol_equa(13))
print(sol_equa(16))
print(sol_equa(17))

