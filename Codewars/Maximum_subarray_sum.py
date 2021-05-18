# def max_sequence(arr):
def getletters(text):
    # return [[sum(arr[i:j]) for j in arr] for i in j]
    return "".join(letter for word in text for letter in word)

    # letter for word in text for letter in word


# print(max_sequence([]))
# print(max_sequence([4,-1,2,1]))
# print(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]))

print(getletters("This is a text with a bunch of words"))
