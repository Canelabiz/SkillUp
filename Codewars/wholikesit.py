# CodeWars Who likes it?


def likes(names):

    n = len(names)

    return {
        0: "no one likes this",
        1: f"{*names} likes this",
        2: f"{*names} and {*names} like this",
        3: f"{*names}, {*names} and {*names} like this",
        4: f"{*names}, {*names} and {len(names) - 2} like this",
    }[min(4, n)]

    """
    return (
        "no one likes this"
        if not names
        else "".join(names) + " likes this"
        if len(names) == 1
        else names[0] + " and " + names[1] + " like this"
        if len(names) == 2
        else names[0] + ", " + names[1] + " and " + names[2] + " like this"
        if len(names) == 3
        else names[0]
        + ", "
        + names[1]
        + " and "
        + str(len(names) - 2)
        + " others like this"
    )
    """


print(likes([]))  # 'no one likes this'
print(likes(["Peter"]))  # 'Peter likes this'
print(likes(["Jacob", "Alex"]))  # 'Jacob and Alex like this'
print(likes(["Max", "John", "Mark"]))  # 'Max, John and Mark like this'
print(likes(["Alex", "Jacob", "Mark", "Max"]))  # 'Alex, Jacob and 2 others like this'
