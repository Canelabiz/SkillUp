def count(string):
    # The function code should be here
    # return dict([letter, int(string.count(letter))] for letter in string)
    return {i: string.count(i) for i in string}


print(count("aba"))
print(count(""))
print(count("uncopyrightable"))
print(count("elephant"))
