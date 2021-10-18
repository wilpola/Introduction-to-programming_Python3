# @author: Ville Wilpola
# @date: 2021-10-08
# @score: 

"""
Assignment:
Write program code that calculates and outputs the factorial of variable n (n is already initialized). For example factorial of 5 is 5*4*3*2*1 = 120.
"""
import random

def factorial(n):
    arr = []
    total = n
    while n != 1:
        z = n - 1
        total = total * z
        arr.append(total)
        n = z
    print(total)
    # print(arr)



numbers = list(range(1,10))

for i in range(0,5):
  number = random.choice(numbers)
  if number in numbers:
    numbers.remove(number)
  print ("Factorial of",number,"is:", factorial(number))