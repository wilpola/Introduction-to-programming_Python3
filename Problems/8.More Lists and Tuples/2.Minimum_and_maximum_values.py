# @author: Ville Wilpola
# @date: 11-23-2021
# Score: 10/10
import random

def minimum_maximum(integer_list):
    _min = 0
    _max = 0

    for i in integer_list:
        if i > _max:
            _max = i
        if i < _min:
            _min = i

    tupl = (_min, _max)
    return tupl


l = []
for i in range(random.randint(15,25)):
  l.append(random.randint(-150,150))

print(" ") 
print ("List:", l)
print ("Minimum and maximum:",minimum_maximum(l))