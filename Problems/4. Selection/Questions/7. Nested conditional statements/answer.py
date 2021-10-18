""" Yet another example about conditional statements. Note how important the proper intendation is when multiple conditional statements with alternative block are combined"""

def main():
    a = 470
    b = 420
    c = 440

    if a > b:
        if a > c:
            print("A is greater than b and c: ", a)
        else:
            print(c)
    else:
        if b > c:
            print("b is greater than a and c: ", b)
        else:
            print("b is greater than a but less than c: ", c)


main()