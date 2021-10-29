# @author: Ville Wilpola
# @date: 2021-10-29
# Score: 10/10

lst = [-1, 2, -12, 23, 24, -324, -8, 1, 4]
def count_positive_items(lst):
    n = 0
    for item in lst:
        if item > 0:
            n = n + 1
    print(n)
    return n

count_positive_items(lst)
print()