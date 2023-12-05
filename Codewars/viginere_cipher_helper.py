# # [Training on Vigenère Cipher Helper | Codewars](https://www.codewars.com/kata/52d1bd3694d26f8d6e0000d3/train/python)


class VigenereCipher(object):
    def __init__(self, key: str, alphabet: str):
        self.key = "".join(key[alphabet.index(i) % len(key)] for i in alphabet)
        self.alphabet = alphabet

    def encode(self, text: str) -> str:
        # return "".join(
        #     self.alphabet[
        #         (self.alphabet.find(c) + self.alphabet.find(self.key.index(c)))
        #         % len(self.alphabet)
        #     ]
        #     for c in text
        # )
        x = ""
        for c in text:
            print(self.key.index(self.alphabet.find(c)))

    def decode(self, text: str) -> str:
        pass


# # Test

abc = "abcdefghijklmnopqrstuvwxyz"
key = "password"
c = VigenereCipher(key, abc)


print(c.encode("codewars"), "rovwsoiv")
# print(c.decode('rovwsoiv'), 'codewars')
print(c.encode("waffles"), "laxxhsj")
# print(c.decode('laxxhsj'), 'waffles')
print(c.encode("CODEWARS"), "CODEWARS")
# print(c.decode('CODEWARS'), 'CODEWARS')
