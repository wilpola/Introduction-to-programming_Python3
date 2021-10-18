""" Program generates three random numbers and stores them into three variables, n1, n2 and n3. Finish the program by outputting the middle one of the numbers. For example, if the values are 11, 22 an 7, you should output 11. Use if and else constructions. Do not use sort() function.

 
Do not  not output anything else but the number! """
import random

def output_middle(n1, n2, n3):
    print("")
    arr = []
    # print("n1: ", n1, "\nn2: ", n2, "\nn3: ", n3)

    arr.append(n1)

    # print("Array", arr)
    [ arr.append(n2) if n2 > n1 else arr.insert(0, n2)]
    # print("Array with n2: ", arr)

    if arr[0] == n1 and n3 > n1:        # if n1 is arr[0] and greater than n1
        if n3 > n2:                     # if n1, n2, n3
            arr.append(n3)              # push to the end of the arr
        else:
            arr.insert(1, n3)
    elif arr[0] == n2 and n3 > n2:      # if n2 is arr[0] and greater than n2
        if n3 > n1:
            arr.append(n3)
        else:
            arr.insert(1, n3)
    else:                               # if every other case fails, we know that n3 is the smallest
        arr.insert(0, n3)


    # print("Array with n3: ", arr)
    print(arr[1])
    

for i in range(0,4):
    n1 = random.randint(50,150) 
    n2 = random.randint(50,150) 
    n3 = random.randint(50,150)
    print ("The numbers are:",n1,n2,n3)
    print ("The middle one is", end = " ")
    output_middle(n1,n2,n3)




    #  Logic
    # 1. arr[0] = n1
    # 2. if n2 > n1 -> arr[1] = n2
    # 3. else if n2 < n1 arr[0] = n2
    # 4. if n3 < n1 and arr[0] == n1 -> arr.insert(0, n3)
    # 5. if n3 < n1 and arr[0] != n1 -> if n3 > arr[0]