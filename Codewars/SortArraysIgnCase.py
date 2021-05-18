""" CodeWars - Sort Arrays (Ignoring Case)

Sort the given strings in alphabetical order, case insensitive. """


def sortme(words):
    return sorted(words, key=str.lower)
    # sort on index char in string for string in list


print(sortme(["Hello", "there", "I'm", "fine"]))
print(sortme(["C", "d", "a", "B"]))
print(sortme(["CodeWars"]))
