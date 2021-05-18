"""
CodeWars - Write out numbers
https://www.codewars.com/kata/52724507b149fa120600031d/train/python

Create a function that transforms any positive number to a string representing the number in words. The function should work for all numbers between 0 and 999999.

three
thirteen
thirty
thirty-seven
eight
eighteen
Twenty-eight
eighty
eighty-eight
two thousand seven hundred forty-nine
ninety-nine thousand nine hundred ninety-nine
"""


"zero one two three four five six seven eight nine ten eleven twelve thir fif eigh teen twen ty fif hundred thousand -"

list(range(0, 9))         # zero - nine
list(range(10, 12 + 1))       # ten, eleven, twelve
list(range(13, 15 + 1, 2)) # thirteen & fifteen
[14].append(list(range(16, 19 + 1))) # fourteen,  sixteen - nineteen

"""
x  = zero - nine
xx = ten, eleven, twelve, thir +, four +, fif +, six +, - nine + teen 
     twen + ty + zero - nine
     thir + - four + ty + zero - nine
     fif + ty + zero - nine
     six + - nine + ty + zero - nine
     one + - nine + hundred
     one + - nine + thousand
     ten +, eleven +, twelve +, thir ++ , four++ , fif ++, six++ - nine ++ teen + thousand
     twen +, thir +, four +, fif +, six+, - nine + ty + one - nine, + thousand
     one + - nine + hundred + thousand

"""
l = list(range(20 + 1))
l.append()
a = {}

def number2words(n):
    """ works for numbers between 0 and 999999 """
    




print(number2words(0))
print(number2words(1))
print(number2words(8))
print(number2words(10))
print(number2words(19))
print(number2words(20))
print(number2words(22))
print(number2words(54))
print(number2words(80))
print(number2words(98))
print(number2words(100))
print(number2words(301))
print(number2words(793))
print(number2words(800))
print(number2words(650))
print(number2words(1000))
print(number2words(1003))