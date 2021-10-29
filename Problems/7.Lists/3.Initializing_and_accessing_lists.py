def main():
    a = [0] * 3
    output(a)
    a[0] = 1
    a[1] = a[0] * 4 + 2
    a[2] = 8 - a[a[0]]
    output(a)

def output(n):
    for i in range(0, len(n), 1):
        print(n[i])

main()