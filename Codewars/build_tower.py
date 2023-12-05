# [Training on Build Tower | Codewars](https://www.codewars.com/kata/576757b1df89ecf5bd00073b/train/python)

# [
#     "  *  ",
#     " *** ",
#     "*****",
# ]

# [
#     "     *     ",
#     "    ***    ",
#     "   *****   ",
#     "  *******  ",
#     " ********* ",
#     "***********",
# ]


def tower_builder(n_floors):
    # SOL 1
    # floor = ""
    # floors = []
    # for i in reversed(range(1, n_floors + 1)):
    #     floor = " " * (n_floors - i) + "*".join("*" * i) + " " * (n_floors - i)
    #     floors.append(floor)
    # floors.reverse()
    # return floors

    # SOL 2
    # floors = [
    #     " " * (n_floors - i) + "*".join("*" * i) + " " * (n_floors - i)
    #     for i in reversed(range(1, n_floors + 1))
    # ]
    # floors.reverse()
    # return floors

    # SOL 3
    return [
        " " * (n_floors - i) + "*".join("*" * i) + " " * (n_floors - i)
        for i in range(1, n_floors + 1)
    ]


[
    "     *     ",
    "    ***    ",
    "    *****    ",
    "   *******   ",
    "   *********   ",
    "  ***********  ",
]

print(tower_builder(1))
print(tower_builder(2))
print(tower_builder(3))
print(tower_builder(6))
