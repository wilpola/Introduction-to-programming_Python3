import random

def output_age(name_birth):

  # Shorthad version of writing the print function
  x = 2011 - int(name_birth[-4:])

  print(x)
  return x


first = [ "John", "James", "Bill", "Arnold", "Lisa", "Ann", "Kimberly", "Monica" ]
last = [ "Smith", "Jones", "Williams", "Brown", "Wilson", "Taylor", "Johnson" ]


for i in range(3):
  name = random.choice(first) + " " + random.choice(last)
  name_age = name + ", 19" + str(random.randint(0,99))
  print ("Name and b.year:", name_age)
  # output_age prints here
  print ("Age:", output_age(name_age)) # returning a val in the func. displayes here



  # Call stack

  # 1. define list first
  # 2. define list last

  # 3. Runs the for loop
    # 1. sets name based on first and last name ex. name = John Jones
    # 2. name_age = name variable == John Jones + string(19) + string(random value between 0 & 99)
    # 3. print name_age
    # 4. print ("Age") call function output_age(name_age) -> return where the function gets called