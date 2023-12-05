# # [Training on Smallest possible sum | Codewars](https://www.codewars.com/kata/52f677797c461daaf7000740/train/python)

# ## Description

# Given an array X of positive integers,
# its elements are to be transformed by running the following operation on them as many times as required:

# `if X[i] > X[j] then X[i] = X[i] - X[j]`

# When no more transformations are possible, return its sum ("smallest possible sum").

# For instance, the successive transformation of the elements of input X = [6, 9, 21] is detailed below:

# ```sh
# X_1 = [6, 9, 12] # -> X_1[2] = X[2] - X[1] = 21 - 9
# X_2 = [6, 9, 6]  # -> X_2[2] = X_1[2] - X_1[0] = 12 - 6
# X_3 = [6, 3, 6]  # -> X_3[1] = X_2[1] - X_2[0] = 9 - 6
# X_4 = [6, 3, 3]  # -> X_4[2] = X_3[2] - X_3[1] = 6 - 3
# X_5 = [3, 3, 3]  # -> X_5[1] = X_4[0] - X_4[1] = 6 - 3
# ```

# The returning output is the sum of the final transformation (here 9).

# ## Example

# `solution([6, 9, 21]) #-> 9`

# ## Solution steps:

# ```sh
# [6, 9, 12] #-> X[2] = 21 - 9
# [6, 9, 6] #-> X[2] = 12 - 6
# [6, 3, 6] #-> X[1] = 9 - 6
# [6, 3, 3] #-> X[2] = 6 - 3
# [3, 3, 3] #-> X[1] = 6 - 3
# ```

# ## Additional notes:

# There are performance tests consisted of very big numbers and arrays of size at least 30000. Please write an efficient algorithm to prevent timeout.

# # Code


def solution(a):
    while sum(a) / len(a) != (a)[0]:
        a = sorted(a)
        a[-1] = (a)[-1] - (a)[-2]
    return sum(a)


# # Test

print((solution([9]), 9))
print((solution([6, 9, 21]), 9))
print((solution([1, 21, 55]), 3))

[1, 21, 55]  # 55 - 21 = 34
[1, 21, 34]  # 34 - 21 = 13
[1, 21, 13]  # 21 - 13 = 8
[1, 8, 13]  # 13 - 8 = 5
[1, 8, 5]  # 8 - 5 = 3
[1, 3, 5]  # 5 - 3 = 2
[1, 3, 2]  # 3 - 2 = 1
[1, 1, 2]  # 2 - 1 = 1
[1, 1, 1]  # Sum = 3
