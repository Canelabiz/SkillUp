""" CodeWars - Counting Duplicates """


def duplicate_count(text):
    return len(1 for c in set(text) if text.count(c) > 1)
    # [text.count(c) for c in set(text) if text.count(c) > 1]
    count = 0
    for c in set(text):
        if text.count(c) > 1:
            count += 1
    return count


print(duplicate_count("abcde"))
print(duplicate_count("abcdea"))
print(duplicate_count("indivisibility"))
