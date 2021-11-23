import random

def get_largest_value(d):
    print(" ")

    return max(d.values())



def test():
    d = {}
    for i in range(random.randint(10,15)):
        key = random.randint(1,1000)
        value = random.randint(-100,100)
        d[key] = value
    print ("Dictionary:", d)
    print ("Largest value:", get_largest_value(d))
    
for i in range(3):
    test()