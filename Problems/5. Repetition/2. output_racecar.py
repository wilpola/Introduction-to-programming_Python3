# @author: Ville Wilpola
# @date: 2021-10-08
# @score: 10/10
def main():
    r = ""
    s = "rac"
    n = ""
    for i in range(0, len(s), 1):
        r = r + s[i]
        n = s[i] + n

    print(r + "e" + n)
main()