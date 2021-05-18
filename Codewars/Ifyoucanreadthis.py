# CodeWars If you can read this...

nato = {
    "a": "Alfa",
    "b": "Bravo",
    "c": "Charlie",
    "d": "Delta",
    "e": "Echo",
    "f": "Foxtrot",
    "g": "Golf",
    "h": "Hotel",
    "i": "India",
    "j": "Juliett",
    "k": "Kilo",
    "l": "Lima",
    "m": "Mike",
    "n": "November",
    "o": "Oscar",
    "p": "Papa",
    "q": "Quebec",
    "r": "Romeo",
    "s": "Sierra",
    "t": "Tango",
    "u": "Uniform",
    "v": "Victor",
    "w": "Whiskey",
    "x": "Xray",
    "y": "Yankee",
    "z": "Zulu",
    " ": "",
    ".": ".",
    "!": "!",
    "@": "@",
    "#": "#",
    "&": "&",
    "(": "(",
    ")": ")",
    "–": "–",
    "[": "[",
    "{": "{",
    "}": "}",
    "]": "]",
    ":": ":",
    ";": ";",
    "'": "'",
    ",": ",",
    "?": "?",
    "/": "/",
    "*": "*",
    '"': '"',
}


def to_nato(words):
    return " ".join(nato[c] for w in words.lower().split() for c in w)
    # return " ".join(nato.get(c, " ") for c in words.lower().split())


print(to_nato("If you can read"))
print(to_nato("Did not see that coming"))
