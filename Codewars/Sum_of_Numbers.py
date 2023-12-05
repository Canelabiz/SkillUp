# [Beginner Series #3 Sum of Numbers](https://www.codewars.com/kata/55f2b110f61eb01779000053)


def get_sum(a, b):
    return sum(range(sorted([a, b])[0], sorted([a, b])[-1] + 1))


# [].sort()
# sorted([])
print(get_sum(0, 1))
