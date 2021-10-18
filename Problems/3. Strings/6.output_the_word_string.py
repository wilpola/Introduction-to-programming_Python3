"""
Arrange the code lines in the program in order, where the program will output the letters in the word 'string'. Each letter is output in it's own line.
"""

def main():
    s = "train song"
    r = s[6:]
    t = r[2:3]
    print(r, t)


    print("------------")

    print(r[0])
    print(s[4 - len(r): 1])
    print(s[1])
    print(s[2 + len(t)])
    print(t)
    t = r[2:]
    print(t[1])

main()