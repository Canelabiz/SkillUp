""" CodeWars - Harshad or Niven numbers
https://www.codewars.com/kata/54a0689443ab7271a90000c6/train/python
"""

class Harshad:
    @staticmethod
    def is_valid(number):

        for i in str(number):
            if i
                
        # Good Luck!

    @staticmethod
    def get_next(number):
        pass
        # Good Luck!

    @staticmethod
    def get_series(count, start=0):
        pass
        # Good Luck!


print("Harshad.is_valid")
print(Harshad.is_valid(1), True, "1 is a valid Harshad number")
print(Harshad.is_valid(18), True, "18 is a valid Harshad number")
print(Harshad.is_valid(19), False, "19 is not a valid Harshad number")
print("Harshad.get_next")
print(Harshad.get_next(0), 1, "The first Harshad number after 0 is 1")
print(Harshad.get_next(1), 2, "The first Harshad number after 1 is 2")
print(Harshad.get_next(17), 18, "The first Harshad number after 17 is 18")
print("Harshad.get_series")
print(
    Harshad.get_series(10),
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "It should return the first 10 Harshad numbers",
)
print(
    Harshad.get_series(20),
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 18, 20, 21, 24, 27, 30, 36, 40, 42],
    "It should return the first 20 Harshad numbers",
)
print(
    Harshad.get_series(10, 1000),
    [1002, 1008, 1010, 1011, 1012, 1014, 1015, 1016, 1017, 1020],
    "It should return the first 10 Harshad numbers after 1000",
)
