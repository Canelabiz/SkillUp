# [Is this a triangle?](https://www.codewars.com/kata/56606694ec01347ce800001b)


def is_triangle(a: int, b: int, c: int) -> bool:
    return max(a, b, c) < a + b + c - max(a, b, c)
