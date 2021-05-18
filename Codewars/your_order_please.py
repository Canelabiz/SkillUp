"""CodeWars - Your order, please"""


def order(sentence):
    ord = []
    for word in sentence.split():
        for i in range(1, len(sentence.split())):
            if word.find(str(i)) != -1:
                ord.append(word)
    return ord


print(order("is2 Thi1s T4est 3a"), "Thi1s is2 3a T4est")
print(order("4of Fo1r pe6ople g3ood th5e the2"), "Fo1r the2 g3ood 4of th5e pe6ople")
print(order(""), "")
