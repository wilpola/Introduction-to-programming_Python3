import random
import string

def get_strings(mixed_list):
    print(" ")
    _s_arr = []

    for i in mixed_list:
        if type(i) == str:
            _s_arr.append(i)
    return _s_arr





l = []
s = string.ascii_letters
for i in range(random.randint(15,25)):
   r = random.randint(0,2)
   if r == 0:
     ind = random.randint(0, len(s) -1 )
     l.append(s[ind : ind + random.randint(1, 4) ])
   elif r == 1:
      l.append(random.randint(-50,50))
   else:
      l.append(random.choice([True, False, 1.0 / random.randint(1, 10) ]))

print ("Whole list:", l)
print ("Strings only:" , get_strings(l))