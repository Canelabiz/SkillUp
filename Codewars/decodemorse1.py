import re

MORSECODE = {
    "....": "H",
    ".": "E",
    "-.--": "Y",
    ".---": "J",
    "..-": "U",
    "-..": "D",
    "": " ",
}


def decodeMorse(morse_code):

    # split morse string into a list of morse-words
    x = re.split("\s\s\s", morse_code)

    # split each morse word into list of morse-letters
    y = [re.split("\s", l) for l in re.split("\s\s", morse_code)]

    # this works flatten = [letter for word in y for letter in word]
    # this also works flatten = "".join([MORSECODE[letter] for word in y for letter in word])

    return "".join(
        [
            MORSECODE[letter]
            for word in [
                re.split("\s", morse) for morse in re.split("\s\s", morse_code)
            ]
            for letter in word
        ]
    )


print(decodeMorse(".... . -.--   .--- ..- -.. ."))
