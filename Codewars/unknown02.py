def stock_list(listOfArt, listOfCat):
    quant = 0
    output = ''
    for art in listOfArt:
        for cat in listOfCat:
            if cat == art.split()[0][0]:
                quant += int(art.split()[1])
                output += 

b = ["ABAR 200", "CDXE 500", "BKWR 250", "BTSQ 890", "DRTY 600"]
c = ["A", "B"]
print(stock_list(b, c), "(A : 200) - (B : 1140)")

dict()