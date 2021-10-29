# @author: Ville Wilpola
# @date: 2021-10-29
# Score: 10/10 2nd try

import random
def print_hello():
    print("Hello")

def print_world():
    print("World")

for i in range(0,10):
  if random.randint(0,1) == 0:
    print_hello()
  else:
    print_world()



# saying that there needs to be a new line char is misleading