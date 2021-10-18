def tax(initial):
    _taxValue = round(int(initial) * 0.07, 3)
    print("Value comes from the tax function: ", _taxValue)


def main():
    x = input("Please enter the cost of your order: ")
    tax(x)



main()