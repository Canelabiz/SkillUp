# CodeWars Street Fighter 2 - Character Selection


def street_fighter_selection(fighters, initial_position, moves):

    vertical = {"up": -1, "down": 1}
    horizontal = {"right": 1, "left": -1}
    cursor = list(initial_position)
    chars = []

    for direction in moves:

        if direction in vertical:
            if (cursor[0] == 0 and vertical[direction] == -1) or (
                cursor[0] == 1 and vertical[direction] == 1
            ):
                cursor[0] = cursor[0]
            else:
                cursor[0] += vertical[direction]

        if direction in horizontal:
            cursor[1] += horizontal[direction]
            if cursor[1] == -6:
                cursor[1] = 0
            if cursor[1] == 5:
                cursor[1] = -1

        chars.append(fighters[cursor[0]][cursor[1]])

    return chars


fighters = [
    ["Ryu", "E.Honda", "Blanka", "Guile", "Balrog", "Vega"],
    ["Ken", "Chun Li", "Zangief", "Dhalsim", "Sagat", "M.Bison"],
]
opts = ["up", "down", "right", "left"]


print("Character selection")
print("should work with no selection cursor moves")
moves = []
solution = []
if street_fighter_selection(fighters, (0, 0), moves) == solution:
    print(street_fighter_selection(fighters, (0, 0), moves))

print("should go left 8 times")
moves = ["left"] * 8
solution = ["Vega", "Balrog", "Guile", "Blanka", "E.Honda", "Ryu", "Vega", "Balrog"]
if street_fighter_selection(fighters, (0, 0), moves) == solution:
    print(street_fighter_selection(fighters, (0, 0), moves))

print("should go right 8 times")
moves = ["right"] * 8
solution = ["E.Honda", "Blanka", "Guile", "Balrog", "Vega", "Ryu", "E.Honda", "Blanka"]
if street_fighter_selection(fighters, (0, 0), moves) == solution:
    print(street_fighter_selection(fighters, (0, 0), moves))

print("should go up 4 times, always the same")
moves = ["up"] * 4
solution = ["Ryu", "Ryu", "Ryu", "Ryu"]
if street_fighter_selection(fighters, (0, 0), moves) == solution:
    print(street_fighter_selection(fighters, (0, 0), moves))

print("should go down 4 times, always the same")
moves = ["down"] * 4
solution = ["Ken", "Ken", "Ken", "Ken"]
if street_fighter_selection(fighters, (0, 0), moves) == solution:
    print(street_fighter_selection(fighters, (0, 0), moves))

print("should use all 4 directions counter-clockwise twice")
moves = ["down", "right", "up", "left"] * 2
solution = ["Ken", "Chun Li", "E.Honda", "Ryu", "Ken", "Chun Li", "E.Honda", "Ryu"]
if street_fighter_selection(fighters, (0, 0), moves) == solution:
    print(street_fighter_selection(fighters, (0, 0), moves))

print("should use all 4 directions clockwise twice")
moves = ["up", "left", "down", "right"] * 2
solution = ["Ryu", "Vega", "M.Bison", "Ken", "Ryu", "Vega", "M.Bison", "Ken"]
if street_fighter_selection(fighters, (0, 0), moves) == solution:
    print(street_fighter_selection(fighters, (0, 0), moves))

print("should cover all characters")
moves = ["up"] + ["left"] * 6 + ["down"] + ["right"] * 6
solution = [
    "Ryu",
    "Vega",
    "Balrog",
    "Guile",
    "Blanka",
    "E.Honda",
    "Ryu",
    "Ken",
    "Chun Li",
    "Zangief",
    "Dhalsim",
    "Sagat",
    "M.Bison",
    "Ken",
]
if street_fighter_selection(fighters, (0, 0), moves) == solution:
    print(street_fighter_selection(fighters, (0, 0), moves))
