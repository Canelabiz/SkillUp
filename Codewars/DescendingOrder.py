def descending_order(num):
    # return int("".join(sorted([i for i in str(num)], reverse=True)))
    return int("".join(sorted(str(num), reverse=True)))


print(descending_order(0))
print(descending_order(15))
print(descending_order(12345789))
