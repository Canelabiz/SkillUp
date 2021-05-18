def get_middle(s):
    return s[(len(s) - 1) / 2 : len(s) / 2 + 1]
    """
    return (
        s[len(s) // 2]
        if len(s) % 2 != 0
        else s[int((len(s) - 1) / 2) : int(((len(s) - 1) / 2) + 2)]
    )
    """


print(get_middle("test"))
print(get_middle("testing"))
print(get_middle("middle"))
print(get_middle("A"))
print(get_middle("of"))
