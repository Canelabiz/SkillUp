"""
CodeWars - Simple fraction to mixed number converter
https://www.codewars.com/kata/556b85b433fb5e899200003f/train/python
"""


def mixed_fraction(s):
    division = [int(i) for i in s.split('/')]
    if division[1] == 0:
        return "cannot divide by 0"
    elif division[0] % division[1] != 0:
        numerator, denominator = divmod(division[0] / division[1], 1)
        fraction_num, fraction_den = denominator.as_integer_ratio()
        return str(f"{int(numerator)} {int(fraction_num)}/{int(fraction_den)}")
    else:
        return int(division[0] / division[1])

    # return (int(s.split('/')[0]) / int(s.split('/')[1]) if int(s.split('/')[0]) % int(s.split('/')[1]) == 0)


print(mixed_fraction('2/3'))
print(mixed_fraction('10/2'))
print(mixed_fraction('6/3'))
print(mixed_fraction('42/2'))
print(mixed_fraction('42/9'))
print(mixed_fraction('6/3'))
print(mixed_fraction('5/0'))
print(mixed_fraction('4/6'))
print(mixed_fraction('0/18891'))
print(mixed_fraction('-10/7'))
print(mixed_fraction('-22/-7'))
