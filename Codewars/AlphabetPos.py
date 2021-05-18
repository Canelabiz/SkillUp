# Codewars Replace With Alphabet Position


def alphabet_position(text):
    alphabet = "a b c d e f g h i j k l m n o p q r s t u v w x y z".split()
    d = dict(zip(alphabet, range(1, len(alphabet) + 1)))
    return " ".join(str(d[i]) for i in text.lower() if i.isalpha())


print(alphabet_position("Hi"))
print(alphabet_position("The sunset sets at twelve o' clock."))
print(alphabet_position("The narwhal bacons at midnight."))
