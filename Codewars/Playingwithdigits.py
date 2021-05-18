# CodeWars - Playing with digits


def dig_pow(n, p):
    return [int(i) ** (p + j) for j in range(len(str(n))) for i in str(n)]
    # return [int(i) ** (p + j) for i in str(n) for j in range(len(str(n)))]

    """
    for i in str(n):
        for j in range(len(str(n))):
            print(int(i) ** (j + p))
    """


print(dig_pow(89, 1))
print(dig_pow(92, 1))
print(dig_pow(46288, 3))
