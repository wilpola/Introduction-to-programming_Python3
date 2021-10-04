# October 4th, 2021
# 10/10

import random


for i in range(3):
    n1 = random.randint(1,10)
    n2 = random.randint(20,30)
    
    print ("n1:",n1)
    print ("n2:",n2)

list1 = []
list2 = []
for i in range((n1), (n2 + 1)):
    list1.append(i)
for i in range((n2), (n1 - 1), -1):
    list2.append(i)


print ("List1:",list1)
print ("List2:",list2)
    
print ("")