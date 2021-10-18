def main():
    a = "Java"
    b = a.replace("a", "ao")
    print(b)
    c = a.replace("a", "")
    print(c)
    print(b[1:3])
    d = a[0] + b[5]
    print("PRINTS D: " + d)
    e = 3 * len(a)
    print("prints e: " + str(e))
    print(d + "k" + "e")
    print(a[2])
main()