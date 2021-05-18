def duplicate_count(text):
    # return sum(1 for c in set(text.lower()) if text.lower().count(c) > 1)
    return len([c for c in set(text.lower()) if text.lower().count(c) > 1])

    """
    otto = 0
    for c in set(text):
        if text.count(c) > 1:
            otto += 1
    return otto
    """


print(duplicate_count("abcde"), 0)
print(duplicate_count("abcdea"), 1)
print(duplicate_count("indivisibility"), 1)
print(duplicate_count("aabbcde"), 2)
print(duplicate_count("aabBcde"), 2)
print(duplicate_count("Indivisibilities"), 2)
print(duplicate_count("aA11"), 2)
print(duplicate_count("ABBA"), 2)
