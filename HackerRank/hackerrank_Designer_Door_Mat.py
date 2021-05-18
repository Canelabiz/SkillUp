# hackerrank_Designer_Door_Mat


# thickness = int(input()) #This must be an odd number
height, width = 7, 21
straight = "-"
pattern = ".|."

# Top
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

# Middle
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))

# Bottom
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c +
          (c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))
