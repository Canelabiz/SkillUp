"""# [CodeWars - Remove First and Last Character](https://www.codewars.com/kata/554e4a2f232cdd87d9000038/train/python))

    It's pretty straightforward.
    Your goal is to create a function that removes the first and last characters of a string.
    You're given one parameter, the original string.
    You don't have to worry with strings with less than two characters.
"""


def remove_char(s: str) -> str:
    return s[1:-1]


print(remove_char("eloquent"), "loquen")
print(remove_char("country"), "ountr")
print(remove_char("person"), "erso")
print(remove_char("place"), "lac")
print(remove_char("ok"), "")
print(remove_char("ooopsss"), "oopss")
