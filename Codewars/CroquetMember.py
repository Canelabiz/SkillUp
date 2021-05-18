def openOrSenior(data):
    # return ["Senior" if data[i][0] >= 55 and data[i][1] > 7 else "Open" for i in range(0, len(data))]
    return [
        "Senior" if age >= 55 and handicap > 7 else "Open" for (age, handicap) in data
    ]


print(openOrSenior([[45, 12], [55, 21], [19, -2], [104, 20]]))
print(openOrSenior([[16, 23], [73, 1], [56, 20], [1, -1]]))

# [[45, 12], [55, 21], [19, -2], [104, 20]]
