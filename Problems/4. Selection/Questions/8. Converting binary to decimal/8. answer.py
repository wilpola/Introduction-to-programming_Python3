"""
The binary numeral system, or base-2 number system, represents numeric values using two symbols, 0 and 1. See this Wikipedia article for more information.
An easy way to convert a binary number into decimal number is use the powers of two. For example:
binary 1010 = 23 + 02 + 11 + 00 = 8 + 0 + 2 + 0 = 10 in decimal
binary 0101 = 03 + 22 + 01 + 10 = 0 + 4 + 0 + 1 = 5 in decimal

In the program below, the variable bin holds a four digit binary number saved into a string. Convert the number into decimal number, and output the decimal value into screen.
HINT: Use the [] operator with strings to check, whether the bits are ones or zeros! 

Note, that since you're completing a function, each line you wrote must have an indent of atleast two spaces in the beginning!
"""

import random

def output_converted(bin):
    print("")
    print("-----> bin: ", bin)

    i = 0
    _loc = int(- len(bin) + 1)
    _decimal = 0 
    arr= []
    
    while i < len(bin):
        _binIndex = int(bin[_loc])
        print("_loc: ", _loc)
        # if _binIndex == 1:
        #     _decimal = _decimal + (_binIndex * (2 ** i))
        #     print("Decimal one: ", _decimal)
        #     i+=1
        # else:
        #     i+=1
        
        arr.append(_binIndex * (2 ** i))
        print("Decimal zero: ", _decimal)
        _loc+=1
        i+=1
    # print("Decimal: ", _decimal)
    print(arr)
        


for i in range(0,4):
  bin = ""
  for j in range(0,4):
    bin += str(random.randint(0, 1))
  print ("Binary string " + bin + " is in decimal:")
  output_converted(bin)