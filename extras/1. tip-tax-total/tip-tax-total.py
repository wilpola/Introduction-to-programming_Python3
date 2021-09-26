"""
@autor Ville Wilpola
# Date: 9/26/2021 Sunday
# Lisence: MIT Lisence
"""

def tip(initial):
    _tipAmount = round(float(initial) * 0.15, 2)
    return _tipAmount

def tax(initial):
    return round(float(initial) * 0.07, 2)

def total(initial, tip, tax):
    return round(float(initial) + tip + tax)


def main():
    print(" ")
    _initialVal = input("Please enter the price of your order: ")
    _tip = float(tip(_initialVal))
    _tax = float(tax(_initialVal))
    _total = float(total(_initialVal, _tax, _tip))

    print("15% tip is "+ str(_tip)+ "€")
    print("7% sales tax is "+ str(_tax)+ "€")
    print("Your total today is: ", str(_total) + "€")

main()

