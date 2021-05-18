import re

MORSE_CODE = {
    "....": "H",
    ".": "E",
    "-.--": "Y",
    ".---": "J",
    "..-": "U",
    "-..": "D",
    " ": " ",
    "": " ",
}


def decodeMorse(morse_code):
    # ToDo: Accept dots, dashes and spaces, return human-readable message

    ############
    # With Regex

    # m_letters = [re.split("\s", m_word) for m_word in re.split("\s\s\s", morse_code)]
    # print(m_letters)
    # morse_code.split

    # v = [MORSE_CODE[letter] for word in m_letters for letter in word]
    # print(v)

    # planets = [['Mercury', 'Venus', 'Earth'], ['Mars', 'Jupiter', 'Saturn'], ['Uranus', 'Neptune', 'Pluto']]

    # Nested List comprehension with an if condition
    # flatten_planets = [planet for sublist in planets for planet in sublist if len(planet) < 6]

    ###############
    # Without Regex

    # Split morse string into list of morse words: '.... . -.--   .--- ..- -.. .'.split("   ") -> ['.... . -.--', '.--- ..- -.. .']
    # morse_words = morse_code.split("   ")

    # Split morse string into list of morse letters: '.... . -.--   .--- ..- -.. .'.split() -> ['....', '.', '-.--', '.---', '..-', '-..', '.']
    # morse_letters = morse_code.split()

    # Create and replace items in list of morse letters with letters:
    # mletters = " ".join(morse_code.split("  ")).split(" ")

    # lst = [MORSE_CODE[letter] for letter in " ".join(morse_code.split("  ")).split(" ")]

    return " ".join(
        "".join(MORSE_CODE[letter] for letter in word.strip().split())
        for word in morse_code.split("   ")
    )

    # debugging:
    # print(f"original message:\t\t\t\t{morse_code}")
    # print(f"Split into list of morse words:\t{morse_words}")
    # print(f"split into morse letters:\t\t{mletters}")
    # print(f"List:\t{lst}")
    # print(f"String:\t{string}")

    """
    return (
        morse_code.replace(".", MORSE_CODE["."])
        .replace("-", MORSE_CODE["-"])
        .replace(" ", "")
    )
    """


print(decodeMorse(".... . -.--   .--- ..- -.. ."))
