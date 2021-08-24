# Codewars - Only-Readable-Once list
# https://www.codewars.com/kata/53f17f5b59c3fcd589000390/train/python


class SecureList:
    def __init__(self, messages) -> None:
        self.data = messages

    def __getitem__(self, idx):
        return self.data.pop(idx)
        # print(self.data.pop(idx))

    def __len__(self):
        return len(self.data)

    def __str__(self):
        s = f"{self.data}"
        self.data.clear()
        return s


base = [1, 2, 3, 4]
a = SecureList(base)

print(a[0], base)
print(a[0], base)
