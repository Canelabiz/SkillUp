def duplicate_encode(word):
    return "".join(
        [")" if word.lower().count(char) > 1 else "(" for char in word.lower()]
    )


print(duplicate_encode("UNCOPYRIGHTABLE"))
print(duplicate_encode("uncopyrightable"))
print(duplicate_encode("din"))
print(duplicate_encode("recede"))
print(duplicate_encode("Success"))
print(duplicate_encode("(( @"))
