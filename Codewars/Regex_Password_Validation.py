""" Codewars - Regex Password Validation """

# You need to write regex that will validate a password to make sure it meets the following criteria:
#
# At least six characters long
# contains a lowercase letter   [a-z]
# contains an uppercase letter  [A-Z]
# contains a number             /d
#
# Valid passwords will only be alphanumeric characters.
#


import re


def regex(pattern):
    regex = re.search(r"[a-z]+", pattern)
    return regex


print(regex("fjd3IR9"))
print(regex("ghdfj32"))
print(regex("DSJKHD23"))
print(regex("dsF43"))
print(regex("4fdg5Fj3"))
print(regex("DHSJdhjsU"))
print(regex("fjd3IR9"))
print(regex("fjd3  IR9"))
print(regex("djI38D55"))
print(regex("a2.d412"))
print(regex("JHD5FJ53"))
print(regex("!fdjn345"))
print(regex("jfkdfj3j"))
print(regex("123"))
print(regex("abc"))
print(regex("123abcABC"))
print(regex("ABC123abc"))
print(regex("Password123"))


"""
gray|grey can match "gray" or "grey".
gray|grey and gr(a|e)y are equivalent patterns which both describe the set of "gray" or "grey".

?	colou?r matches both "color" and "colour".
*	ab*c matches "ac", "abc", "abbc", "abbbc", and so on.
+	ab+c matches "abc", "abbc", "abbbc", and so on, but not "ac".
{n}[19] The preceding item is matched exactly n times.
{min,}[19]	The preceding item is matched min or more times.
{min,max}[19]	The preceding item is matched at least min times, but not more than max times.
.   a.b matches any string that contains an "a", then any other character and then a "b", a.*b matches any string that contains an "a" and a "b" at some later point.

a|b* denotes {ε, "a", "b", "bb", "bbb", ...}
(a|b)* denotes the set of all strings with no symbols other than "a" and "b", including the empty string: {ε, "a", "b", "aa", "ab", "ba", "bb", "aaa", ...}
ab*(c|ε) denotes the set of strings starting with "a", then zero or more "b"s and finally optionally a "c": {"a", "ac", "ab", "abc", "abb", "abbc", ...}
(0|(1(01*0)*1))* denotes the set of binary numbers that are multiples of 3: { ε, "0", "00", "11", "000", "011", "110", "0000", "0011", "0110", "1001", "1100", "1111", "00000", ... }

.at matches any three-character string ending with "at", including "hat", "cat", and "bat".
[hc]at matches "hat" and "cat".
[^b]at matches all strings matched by .at except "bat".
[^hc]at matches all strings matched by .at other than "hat" and "cat".
^[hc]at matches "hat" and "cat", but only at the beginning of the string or line.
[hc]at$ matches "hat" and "cat", but only at the end of the string or line.
\[.\] matches any single character surrounded by "[" and "]" since the brackets are escaped, for example: "[a]" and "[b]".
s.* matches s followed by zero or more characters, for example: "s" and "saw" and "seed".

fjd3IR9
ghdfj32
DSJKHD23
dsF43
4fdg5Fj3
DHSJdhjsU
fjd3IR9
fjd3  IR9
djI38D55
a2.d412
JHD5FJ53
!fdjn345
jfkdfj3j
123
abc
123abcABC
ABC123abc
Password123

"""
