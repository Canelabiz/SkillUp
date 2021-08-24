# Codewars - Alphabet war - airstrike - letters massacre
# https://www.codewars.com/kata/5938f5b606c3033f4700015a/train/python

left = {"w": 4, "p": 3, "b": 2, "s": 1}
right = {"m": 4, "q": 3, "d": 2, "z": 1}


def alphabet_war(fight):
    ...


print(alphabet_war("z"), "Right side wins!")
print(alphabet_war("****"), "Let's fight again!")
print(alphabet_war("z*dq*mw*pb*s"), "Let's fight again!")
print(alphabet_war("zdqmwpbs"), "Let's fight again!")
print(alphabet_war("zz*zzs"), "Right side wins!")
print(alphabet_war("sz**z**zs"), "Left side wins!")
print(alphabet_war("z*z*z*zs"), "Left side wins!")
print(alphabet_war("*wwwwww*z*"), "Left side wins!")
print(alphabet_war("w****z"), "Let's fight again!")
print(alphabet_war("mb**qwwp**dm"), "Let's fight again!")
