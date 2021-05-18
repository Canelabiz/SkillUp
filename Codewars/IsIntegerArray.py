""" CodeWars - Is Integer Array? """


def is_int_array(arr):
    # your code here
    # if type(arr) == "List" and arr > 0:
    return (i for i in arr if i % 2 == 0 if type(arr) == "List" and arr > 0)


print(is_int_array([]), True, "Input: []")
print(is_int_array([1, 2, 3, 4]), True, "Input: [1, 2, 3, 4]")
print(is_int_array([-11, -12, -13, -14]), True, "Input: [-11, -12, -13, -14]")
print(is_int_array([1.0, 2.0, 3.0]), True, "Input: [1.0, 2.0, 3.0]")
print(is_int_array([1, 2, None]), False, "Input: [1,2, None]")
print(is_int_array(None), False, "Input: None")
print(is_int_array(""), False, "Input: ''")
print(is_int_array([None]), False, "Input: [None]")
print(is_int_array([1.0, 2.0, 3.0001]), False, "Input: [1.0, 2.0, 3.0001]")
print(is_int_array(["-1"]), False, "Input: ['-1']")
