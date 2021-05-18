def binary_array_to_number(arr):
    # return int("".join(arr), 2)
    # return "".join(arr)
    return int("".join([str(i) for i in arr]), 2)


print(binary_array_to_number([0, 0, 0, 1]))
print(binary_array_to_number([0, 0, 1, 0]))
print(binary_array_to_number([1, 1, 1, 1]))
print(binary_array_to_number([0, 1, 1, 0]))
