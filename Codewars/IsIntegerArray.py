""" CodeWars - Is Integer Array? """


def is_int_array(arr):
    # SOL 1
    # if isinstance(arr, list):
    #     if not arr:
    #         return True
    #     elif [int(i) for i in arr if i] == arr:
    #         return True
    #     else:
    #         return False
    # return False

    # SOL 2
    return isinstance(arr, list) and (
        [int(i) for i in arr if i and isinstance(i, (int, float))] == arr or not arr
    )


print(is_int_array([]))  #    True, "Input: []")
print(is_int_array([1, 2, 3, 4]))  #    True, "Input: [1, 2, 3, 4]")
print(is_int_array([-11, -12, -13, -14]))  #    True, "Input: [-11, -12, -13, -14]")
print(is_int_array([1.0, 2.0, 3.0]))  #    True, "Input: [1.0, 2.0, 3.0]")
print(is_int_array([1, 2, None]))  #    False, "Input: [1,2, None]")
print(is_int_array(None))  #    False, "Input: None")
print(is_int_array(""))  #    False, "Input: ''")
print(is_int_array([None]))  #    False, "Input: [None]")
print(is_int_array([1.0, 2.0, 3.0001]))  #    False, "Input: [1.0, 2.0, 3.0001]")
print(is_int_array(["-1"]))  #    False, "Input: ['-1']")
print(
    is_int_array([240, 311, "pippi", 3, 706, 8, 9, 97, 318, 7, 921, 32, 16, 10, 2, 606])
)  #    False, "Input: [240, 311, 'pippi', 3, 706, 8, 9, 97, 318, 7, 921, 32, 16, 10, 2, 606]")
