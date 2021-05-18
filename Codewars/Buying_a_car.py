# CodeWars - Buying a car
#  https://www.codewars.com/kata/554a44516729e4d80b000012/train/python

# Old car starting price = 2000
# New car starting price = 8000
# Monthly savings = 1000
# Cars price monthly decrease = 1.5%
# Percentage loss bimonthly increase = 0.5%


def nbMonths(startPriceOld, startPriceNew, savingperMonth, percentLossByMonth):
    total_val = 0
    months = 0
    while total_val < startPriceNew:
        total_val = startPriceNew * 




    


print(nbMonths(2000, 8000, 1000, 1.5))
print(nbMonths(12000, 8000, 1000, 1.5))





    # percentLossByMonth += 0.5 if month // 2 != 0
    # startPriceOld * (1 - percentLossByMonth / 100)
    # savingperMonth
    # startPriceNew * (1 - percentLossByMonth / 100)