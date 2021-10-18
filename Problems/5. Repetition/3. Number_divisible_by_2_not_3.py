# @author: Ville Wilpola
# @date: 2021-10-08
# @score: 10/10 =?> 3 attempts.

"""
Assignment:
Program generates two random values, n1 and n2, and outputs them. Your job is to write a loop, which outputs all numbers between (n1,n2) that are divisible by 2 but are NOT divisible by 3.
"""

import random

n1 = random.randint(0, 10)
n2 = random.randint(30, 45)

print("Values of n1, n2: ", n1, ",", n2)

def loop(n1, n2):
    arr = []
    for i in range(n1, (n2 + 1)):
        print(i)
        # if i % 2 == 0 and i % 3 != 0:
        #     # arr.append(i)
        #     print(i)
    # print(arr)

loop(n1, n2)