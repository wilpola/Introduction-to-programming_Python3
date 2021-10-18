def main():
    a = 5
    b = 2
    c = a
    a = b
    b = c
    print("a =", a, "b =", b)

    #9
    result = 4
    print("Result", (result - 2) * (result + 2) // result)

    #10
    a = 10
    b = 4
    c = int(a / b)
    print("The value of c:", c)


main()