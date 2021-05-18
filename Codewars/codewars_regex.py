from re import search

test = [
"fjd3IR9"
"ghdfj32"
"DSJKHD23"
"dsF43"
"4fdg5Fj3"
"DHSJdhjsU"
"fjd3IR9"
"fjd3  IR9"
"djI38D55"
"a2.d412"
"JHD5FJ53"
"!fdjn345"
"jfkdfj3j"
"123"
"abc"
"123abcABC"
"ABC123abc"
"Password123"]


def rere(bip):
    return search("([A-Z]{1,}|[a-z]{1,}|[0-9]{1,}){6,}", 'bip')


for entry in test:
    print(rere(entry))




