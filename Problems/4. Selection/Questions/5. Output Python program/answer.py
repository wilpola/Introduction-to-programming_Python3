""" Arrange the code lines in order where the program outputs \"Python Program\""""

def main():
    a = 3
    b = 5

    s = "Python Program"

    a = b - 1
    b = b - 3
    b = b + a + a % 3
    a = a % 4

    if s[a] == s[b]:
        print(s) 

main()