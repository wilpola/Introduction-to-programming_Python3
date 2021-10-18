def main():
    name = input("Enter your name: ").title()
    print("Good morning, " + name + "!")
    age = int(input("Enter your age: "))
    # print(type(age))
    print("Woah ", age, " is old!")


def binOctHex():
    bnum = 0b1001
    onum = 0o17571423
    xnum = 0x4a4a4a
    print(bnum, '\n', onum, '\n', xnum)

    bnum1 = bin(22)
    onum1 = oct(22)
    xnum1 = hex(22)

    print("The bin of 22 is: ", bnum1) 
    print("The oct of 22 is: ", onum1) 
    print("The hex of 22 is: ", xnum1) 

# main()
binOctHex()