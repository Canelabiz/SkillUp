# CodeWars Title Case
# https://www.codewars.com/kata/5202ef17a402dd033c000009/train/python


def title_case(title, minor_words=""):
    return " ".join(
        word.capitalize()
        if pos == 0 or word.lower() not in minor_words.lower().split()
        else word.lower()
        for pos, word in enumerate(title.split())
    )


print(title_case(""), "")
print(title_case("a clash of KINGS", "a an the of"))  # "A Clash of Kings"
print(title_case("THE WIND IN THE WILLOWS", "The In"))  # "The Wind in the Willows"
print(title_case("the quick brown fox"))  # "The Quick Brown Fox"
print(title_case("First a of in", "an often into"))  # First A Of In
