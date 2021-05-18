# CodeWars Data Reverse
def data_reverse(data):

    return [
        digit
        for byte in [data[i : i + 8] for i in range(0, len(data), 8)][::-1]
        for digit in byte
    ]


data1 = [
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    1,
    1,
    1,
    1,
    1,
    0,
    1,
    0,
    1,
    0,
    1,
    0,
]
data2 = [
    1,
    0,
    1,
    0,
    1,
    0,
    1,
    0,
    0,
    0,
    0,
    0,
    1,
    1,
    1,
    1,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
]
print(data_reverse(data1), data2)

data3 = [0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1]
data4 = [0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0]
print(data_reverse(data3), data4)
