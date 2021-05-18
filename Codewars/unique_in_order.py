"""CodeWars - Unique In Order"""


def unique_in_order(iterable):
    liz = []
    for c in list(iterable):
        liz.append(c)


print(unique_in_order("AAAABBBCCDAABBB"), ["A", "B", "C", "D", "A", "B"])
print(unique_in_order("AAAABBBCCDAABBB"), ["A", "B", "C", "D", "A", "B"])
print(unique_in_order("ABBCcAD"), ["A", "B", "C", "c", "A", "D"])
print(unique_in_order([1, 2, 2, 3, 3]), [1, 2, 3])
