""" 
Sort the items in array m to match the order after executing the following code segment:

m = [3, 5, 2, 1, 4, 7, 6, 8]
for i in range(0, len(m) / 2):
    t = m[i]
    m[i] = m[len(m) - 1 - i]
    m[len(m) - 1 - i] = t
"""

m = [ 3, 5, 2, 1, 4, 7, 6, 8 ]
def main():
    for i in range(0, len(m) / 2): 
        t = m[i]
        m[i] = m[len(m) - 1 - i]
        m[len(m) - 1 - i] = t
    print(t)

main()