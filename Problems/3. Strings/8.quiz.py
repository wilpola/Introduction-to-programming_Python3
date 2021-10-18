def first():
    print(" FIRST ")
    my_string = "this is amazing"
    print(my_string[len(my_string) - 1])

def second():
    print(" SECOND ")
    r = "abcdef"
    r2 = r[0] + r[2] + r[4]
    print(r2)

def third():
    print(" THIRD ")
    my_str = "ababab"
    my_str = my_str.replace(my_str[0], my_str[3])
    print(my_str)

def fourth():
    print(" FOURTH ")
    my_string = "abcde"
    print(my_string[1:len(my_string) - 1])
    print(my_string)

def fifth():
    print(" FIFTH ")
    s = "result:" + str(1+2)
    ln = len(s)
    print(ln)

def sixth():
    print(" SIXTH ")
    a = "Python"
    b = a
    b = a[1:3]
    print(b)

def seventh():
    print()

first()
second()
third()
fourth()
fifth()
sixth()