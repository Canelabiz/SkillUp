# Codewars - Array Deep Count
# https://www.codewars.com/kata/596f72bbe7cd7296d1000029/train/python


def deep_count(a):
    depths = []
    for item in a:
        if isinstance(item, list):
            depths.append(deep_count(item))
    if len(depths) > 0:
        return 1 + max(depths)
    return a

    # if isinstance(a, list):
    #     for sub in a:
    #         yield from deep_count(sub)
    # else:
    #     yield a

    # result = []
    # for item in a:
    #     if isinstance(item, list):
    #         # result.append(deep_count(item))
    #         result.extend(item)
    #     else:
    #         result.append(item)
    # return len(result)

    # return len(y if isinstance(item, list) else item for item in a for y in [item[0]]*item[1])

    # for item in a:
    #     if isinstance(item, list):
    #         yield from deep_count(item)
    #     else:
    #         yield item
    # return item


print(deep_count([]))
print(deep_count([1, 2, 3]))
print(deep_count(["x", "y", ["z"]]))
print(deep_count([1, 2, [3, 4, [5]]]))
print(deep_count([[[[[[[[[]]]]]]]]]))
