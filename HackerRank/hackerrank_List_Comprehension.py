# hackerrank List Comprehension


def main(x: int, y: int, z: int, n: int) -> list:

    # inner = []
    # for i in range(x+1):
    #     for j in range(y+1):
    #         for k in range(z+1):
    #             if i+j+k != n:
    #                 inner.append([i,j,k])
    # return inner

    # return [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k != n]


print(main(1, 1, 1, 2))
print(main(2, 2, 2, 2))
