# [Training on Help the bookseller ! | Codewars](https://www.codewars.com/kata/54dc6f5a224c26032800005c/train/python)


def stock_list(list_of_art, list_of_cat):
    if not list_of_art or not list_of_cat:
        return ""
    stock = {}
    for entry in list_of_art:
        code, quant = entry.split()
        stock[code] = int(quant)

    stock_list = {}
    for cat in list_of_cat:
        in_stock = 0
        for bloop in stock:
            if bloop.startswith(cat):
                in_stock += stock[bloop]
            stock_list[cat] = in_stock

    result_list = []
    for pair in stock_list:
        res_str = f"({pair} : {stock_list.get(pair)})"
        result_list.append(res_str)
        result = " - ".join(result_list)
    return result


b = ["BBAR 150", "CDXE 515", "BKWR 250", "BTSQ 890", "DRTY 600"]
c = ["A", "B", "C", "D"]
print(stock_list(b, c))  # "(A : 0) - (B : 1290) - (C : 515) - (D : 600)"

b = ["ABAR 200", "CDXE 500", "BKWR 250", "BTSQ 890", "DRTY 600"]
c = ["A", "B"]
print(stock_list(b, c))  # "(A : 200) - (B : 1140)"

b = []
c = ["A", "B"]
print(stock_list(b, c))  # ""

b = ["ABAR 200", "CDXE 500", "BKWR 250", "BTSQ 890", "DRTY 600"]
c = []
print(stock_list(b, c))  # ""
