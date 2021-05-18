def solution(n):
    arabic = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    symbol = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    roman = []
    for i in range(len(arabic)):
        count = n // arabic[i]
        roman.append(symbol[i] * count)
        n -= arabic[i] * count
    return "".join(roman)


print(solution(1))
print(solution(4))
print(solution(6))
print(solution(14))
print(solution(21))
print(solution(89))
print(solution(91))
print(solution(984))
print(solution(1000))
print(solution(1889))
print(solution(1989))
