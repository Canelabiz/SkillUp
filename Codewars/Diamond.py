"""
CodeWars Give me a Diamond
https://www.codewars.com/kata/5503013e34137eeeaa001648/train/python
"""


def diamond(n):
    # Make some diamonds!
    return "".join(" " * (n // 2) + i * "*" + "\n" for i in range(1, n + 1, 2))

    # return "".join(
    #     " " * (n // 2) + i * "*" + "\n"
    #     for i in range(1, n)
    #     for i in reversed(range(1, n + 1))
    # )


print(diamond(7))

"""


   *
  ***
 *****
******* 7
 *****
  ***
   *


       *
      ***
     *****
    *******
   *********
  ***********
 *************
*************** 15
 *************
  ***********
   *********
    *******
     *****
      ***
       *

print(diamond(1))
print(diamond(2))
print(diamond(3))
print(diamond(5))
print(diamond(0))
print(diamond(-3))

"""
