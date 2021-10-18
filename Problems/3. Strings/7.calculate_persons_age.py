"""
Python has a function int(s), which parses an integer value out of a given string s. For example, the following program..
 
s = "12" + "3" # s == "123"
n = int(s) # value of n is 123
n = n + 10 # int value can be used in arithmetic expression
print (n) # Output 133
 

 
...would output 123. In program below, the variable nameBirth references a String with a person's name and a birth year (for example "John Smith, 1981"). Calculate and output the person's age in the year 2011. Do not write any function definitions, and do not output anything else but the age as a number!. 
 
For example, if the value of  the nameBirth would be 
 
John Smith, 1981
 
...your program should output 30
"""
import random

def output_age(name_birth):
  # long way
  x = [int(s) for s in name_birth.split() if s.isdigit()]
  print(2011 - x[0])

  #short way
  print(2011 - int(name_birth[-4:]))

  # return 2011 - x[0]


first = [ "John", "James", "Bill", "Arnold", "Lisa", "Ann", "Kimberly", "Monica" ]
last = [ "Smith", "Jones", "Williams", "Brown", "Wilson", "Taylor", "Johnson" ];

for i in range(3):
  name = random.choice(first) + " " + random.choice(last)
  name_age = name + ", 19" + str(random.randint(0,99))
  print ("Name and b.year:", name_age)
  print ("Age:", output_age(name_age))