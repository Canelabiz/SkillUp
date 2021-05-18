# Codewars - Autocomplete! Yay!
# https://www.codewars.com/kata/5389864ec72ce03383000484/train/python


# def autocomplete(input_, dictionary):
#     result = []
#     for item in dictionary:
#         if item.startswith(input_):
#             result.append(item)
#     return result[:5]

# from string import punctuation

# def autocomplete(input_, dictionary):
#     return [
#         item
#         for item in dictionary
#         if item.lower().startswith(input_.strip(punctuation).lower())
#     ][:5]

from re import sub


def autocomplete(input_, dictionary):
    return [
        item
        for item in dictionary
        if item.lower().startswith(sub("[^a-zA-Z]+", "", input_.lower()))
    ][:5]


### Test section
print(punctuation)

dictionary = [
    "abnormal",
    "arm-wrestling",
    "absolute",
    "airplane",
    "airport",
    "amazing",
    "apple",
    "ball",
]

print(
    "test: ",
    autocomplete("ai", dictionary),
    "\texpected: ",
    ["airplane", "airport"],
)
print(
    "test: ",
    autocomplete("a", dictionary),
    "\texpected: ",
    ["abnormal", "arm-wrestling", "absolute", "airplane", "airport"],
)
print(autocomplete("^apple", dictionary))
