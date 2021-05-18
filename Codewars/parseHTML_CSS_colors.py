"""
CodeWars - Parse HTML/CSS Colors
https://www.codewars.com/kata/58b57ae2724e3c63df000006/train/python
"""

# list comprehension, create list of pairs from a hexadecimal string value
# [hexstring[i:i+2] for i in range(0,len(hexstring), 2)]
# [color[i : i + 2] for i in range(1, len(color), 2)]

# dict comprehension
# dict_variable = {key:value for (key,value) in dictonary.items()}

# dict comprehension, combine lists
# {test_keys[i]: test_values[i] for i in range(len(test_keys))}
# {rgb[x]: int([color[i : i + 2] for i in range(1, len(color), 2)][x], 16) for x in range(len(rgb))}

# {(some_key if condition else default_key):(something_if_true if condition
#   else something_if_false) for key, value in dict_.items() }

# [int(color[i] + color[i], 16) for i in range(1, len(color))]
# [int([color[i] + color[i] for i in range(1, len(color))][x], 16) for x in range(3)]

rgb = ["r", "g", "b"]
PRESET_COLORS = {
    "limegreen": "#32CD32",
    "red": "#FF0000",
    "green": "#008000",
    "blue": "#0000FF",
}


def parse_html_color(color):

    return {
        rgb[x]: int([color[i : i + 2] for i in range(1, len(color), 2)][x], 16)
        if color.startswith("#") and len(color) > 4
        else int([color[i] + color[i] for i in range(1, len(color))][x], 16)
        if color.startswith("#") and len(color) == 4
        else int(
            [
                PRESET_COLORS[color.lower()][i : i + 2]
                for i in range(1, len(PRESET_COLORS[color.lower()]), 2)
            ][x],
            16,
        )
        for x in range(len(rgb))
    }

    # if color.startswith("#") and len(color) > 4 elif color.startswith("#") and len(color) == 4


print(parse_html_color("#80FFA0"), {"r": 128, "g": 255, "b": 160})
print(parse_html_color("#3B7"), {"r": 51, "g": 187, "b": 119})
print(parse_html_color("LimeGreen"), {"r": 50, "g": 205, "b": 50})

# [int(PRESET_COLORS[color][i:i+2], 16) for i in range(1, len(PRESET_COLORS[color])[x],2)]
