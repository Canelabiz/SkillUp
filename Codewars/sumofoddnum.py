def row_sum_odd_numbers(n):
    # return sum([odd for odd in range(n * (n - 1) + 1, n * n + n) if odd % 2 != 0])
    return n ** 3


print((row_sum_odd_numbers(1)))
print((row_sum_odd_numbers(2)))
print((row_sum_odd_numbers(13)))
print((row_sum_odd_numbers(19)))
print((row_sum_odd_numbers(41)))

# n * (n - 1) + 1 , n * n + (n-1)
