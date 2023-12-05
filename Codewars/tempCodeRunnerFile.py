def high(x):
    word_points = {}
    for word in x.split():
        points = 0
        for char in word.lower():
            if char.isalpha():
                points += table[char]
        word_points[word] = points
    return max(word_points, key=word_points.get)
