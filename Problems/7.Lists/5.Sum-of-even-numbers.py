# @author: Ville Wilpola
# @date: 2021-10-29
# Score: 10/10

import random

def sum_of_even(l):
    print(" ")
    total = 0
    for i in range(len(l)):
        if (l[i] % 2) == 0:
            total = total + l[i]
            print(i, ":",l[i], total)

    return total


l = []
for i in range(0, random.randrange(18,25)):
  l.append(random.randrange(1,16))
  
print ("List:",l)
print ("Sum of even values:",sum_of_even(l))