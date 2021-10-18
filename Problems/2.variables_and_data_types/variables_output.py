"""
Assignment:
Arrange the program code lines in such order that the program outputs values (10, 100, 1000, 10000) in order from smallest to largest.
"""

def main():
    print("//--------------//")

    a = 0
    b = 1
    c = 2

    # Reorder the following
    print(a * c + b * 10)
    a = b * 10
    c = a * a
    b = c * c
    print(a * a)
    print(b / c * a) 
    print(b)


    

# Run the function
main()