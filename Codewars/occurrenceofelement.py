"""
CodewarsSimple Delete occurrences of an element if it occurs more than n times
https://www.codewars.com/kata/554ca54ffa7d91b236000023/train/python
"""


def delete_nth(order, max_e):
    r_ = []
    for i in order:
        if order.count(i) <= max_e:
            print(f"The amount of {i}'s <= {max_e}")
            r_.append(i)
        else:
            print(f"The amount of {i}'s > {max_e}")
            order.remove(i)
    return r_


print(delete_nth([20, 37, 20, 21], 1), "Should be", [20, 37, 21])
print(delete_nth([1, 1, 3, 3, 7, 2, 2, 2, 2], 3), "Should be", [1, 1, 3, 3, 7, 2, 2, 2])
