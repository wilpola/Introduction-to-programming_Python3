# @author: Ville Wilpola
# @date: 2021-10-08
# @score: 

"""
Assignment:

Arrange code lines so that the program prints out three multiplications (1 * 2, 2 * 4 and 3 * 8) and their results.

 
The syntax used in print statements
 
print ("a string", end="")
 
...means that the next outputted line is concatenated after this line. Moreover, the end="" part discards the excessive space at the end of the line caused by the comma operator.
"""
def main():
    a = 1
    b = 2

    while a + b < 12:
        print(a * b)
        print(" * ", end = "")
        a = a + 1
        print(b + " = ", end = "")
        b = b * 2
        print(a, end = "")
main()