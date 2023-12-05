# [Training on The observed PIN | Codewars](https://www.codewars.com/kata/5263c6999e0f40dee200059d/train/python)

adjecent = [
    [0, 2],
    [1, 2, 4],
    [1, 2, 3, 5],
    [2, 3, 6],
    [1, 4, 5, 7],
    [2, 4, 5, 6, 8],
    [3, 5, 6, 9],
    [4, 7, 8],
    [5, 7, 8, 9, 0],
    [6, 8, 9],
]


def get_pins(observed):
    otto = []
    for idx in list(observed):
        for digit in adjecent[int(idx)]:
            otto.append()

    # return [str(digit) for idx in observed for digit in adjecent[int(idx)]]


print(get_pins("8"), ["5", "7", "8", "9", "0"])
print(get_pins("11"), ["11", "22", "44", "12", "21", "14", "41", "24", "42"])
print(
    get_pins("369"),
    [
        "339",
        "366",
        "399",
        "658",
        "636",
        "258",
        "268",
        "669",
        "668",
        "266",
        "369",
        "398",
        "256",
        "296",
        "259",
        "368",
        "638",
        "396",
        "238",
        "356",
        "659",
        "639",
        "666",
        "359",
        "336",
        "299",
        "338",
        "696",
        "269",
        "358",
        "656",
        "698",
        "699",
        "298",
        "236",
        "239",
    ],
)
