def find_next_square(sq):
    # Return the next square if sq is a square, -1 otherwise
    return ((sq**0.5) + 1) ** 2 if int(sq**0.5) == sq**0.5 else -1


find_next_square(121)  # 144, "Wrong output for 121"
find_next_square(625)  # 676, "Wrong output for 625"
find_next_square(319225)  # 320356, "Wrong output for 319225"
find_next_square(15241383936)  # 15241630849, "Wrong output for 15241383936"


# def permutations(s):
#     if len(s) <= 1:
#         yield s
#     else:
#         for i in range(len(s)):
#             for permutation in permutations(s[:i] + s[i + 1 :]):
#                 yield s[i] + permutation

# def permutations(s):
#     result = []
#     if len(s) <= 1:
#         return [s]
#     for i in range(len(s)):
#         for permutation in permutations(s[:i] + s[i + 1 :]):
#             result.append (s[i] + permutation)
#     return result


def permutations(s):
    result = []
    if len(s) <= 1:
        return [s]
    for i in range(len(s)):
        result.extend(
            s[i] + permutation for permutation in permutations(s[:i] + s[i + 1 :])
        )
    return set(result)


print(permutations("abca"))
