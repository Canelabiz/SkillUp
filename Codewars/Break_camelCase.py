# CodeWars - Break camelCase


def solution(s):
    # return "".join(c if c.islower() == True else " " + c for c in s)
    return "".join(c if c.islower() else " " + c for c in s)


print(solution("helloWorld"))
print(solution("camelCase"))
print(solution("breakCamelCase"))
