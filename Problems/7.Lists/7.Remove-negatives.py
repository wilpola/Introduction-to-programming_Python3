# @author: Ville Wilpola
# #date: 2021-10-29
# Score: ?/10

import random

def remove_negatives(l):
    print(" ")
    # new_l = []
    # for i in range(len(l)):
    #     if l[i] >= 0:
    #         print(i, ':', l[i])
    #         new_l.append(l[i])
    # print(new_l)
    # l = new_l
    # print("new list:", l)
    # l = [i for i in new_l]
    # print("L", l)
    # return l[:]
    
    # new_l = l[:]
    # for i in l:
    #     if i < 0:
    #         new_l.remove(i)
    # l = new_l[:]
    # return l

    return filter( lambda x: x>=0, l)
    

l = []
for i in range(0, random.randint(15,25)):
  l.append(random.randint(-15,15))

print ("Before:", l)
remove_negatives(l)
print ("After:", l)