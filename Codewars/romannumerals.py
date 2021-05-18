def solution(n):
    if 1000 <= n <= 3999:
        s = (n // 1000) * "M"
        solution(n - (n // 1000) * 1000)
    elif 900 <= n <= 999:
        s = "CM"
        solution(n - 900)
    elif 600 <= n <= 899:
        s = "D" + ((n - 500) // 100) * "C"
        solution(n - (n // 100) * 100)
    elif 500 <= n <= 599:
        s = "D"
        solution(n - 500)
    elif 400 <= n <= 499:
        s = "CD"
        solution(n - 400)
    elif 100 <= n <= 399:
        s = (n // 100) * "C"
        solution(n - (n // 100) * 100)
    elif 90 <= n <= 99:
        s = "XC"
        solution(n - 90)
    elif 60 <= n <= 89:
        s = "L" + ((n - 50) // 10) * "X"
        solution(n - (n // 10) * 10)
    elif 50 <= n <= 59:
        s = "L"
        solution(n - 50)
    elif 40 <= n <= 49:
        s = "XL"
        solution(n - 40)
    elif 10 <= n <= 39:
        s = (n // 10) * "X"
        solution(n - (n // 10) * 10)
    elif n == 9:
        s = "IX"
    elif 6 <= n <= 8:
        s = "V" + (n - 5) * "I"
    elif n == 5:
        s = "V"
    elif n == 4:
        s = "IV"
    elif 1 <= n <= 3:
        s = n * "I"
    return s


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
