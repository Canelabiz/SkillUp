# hackerrank String Validators

def alnum(text):
    count = 0
    for char in text:
        if char.isalnum():
            count += 1
    if count > 0:
        return True
    else:
        return False


def alpha(text):
    count = 0
    for char in text:
        if char.isalpha():
            count += 1
    if count > 0:
        return True
    else:
        return False


def digit(text):
    count = 0
    for char in text:
        if char.isdigit():
            count += 1
    if count > 0:
        return True
    else:
        return False


def lower(text):
    count = 0
    for char in text:
        if char.islower():
            count += 1
    if count > 0:
        return True
    else:
        return False


def upper(text):
    count = 0
    for char in text:
        if char.isupper():
            count += 1
    if count > 0:
        return True
    else:
        return False


if __name__ == '__main__':
    s = input()
    print(alnum(s))
    print(alpha(s))
    print(digit(s))
    print(lower(s))
    print(upper(s))
