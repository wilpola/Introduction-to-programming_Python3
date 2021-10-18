# STRING DATA TYPE
# strings are arrays of bytes representing unicode characters
s1="text" # string is created with double quotation marks
s2='this is also a string' # single quotation marks are the same thing
s3='abc123!# "/(@£$..   ""abc123ABC' # strings can contain any characters
s4="""one liner""" # three " or '-characters indicates a multiline string
s5= """line1
line2
line3
the last line is here"""  # a multiline string can cover multiple lines

# individual characters are accessed by indexing with square brackets
a = "text" # string that contains 4 characters
a[0] # the indexing start from zero, similar to lists and tuples
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(len(a)) # len() built-in function returns the number of characters in a string
a[0] # the index 0 is always the first element of a string...
a[len(a)-1] # ...so the index len(a)-1 is always the last element

a[-1] # negative indexing means counting elements from the end
print(a[-1]) # negative indices start from -1
print(a[-2])
print(a[-3])
print(a[-4])
# notice that a[-1] is always the same element as a[len(a)-1]

# strings are unchangeable, so the elements cannot be changed
# a[0]=6 this would create an error, because strings are unchangeable





# SLICING
# characters of strings can be taken with square brackets [] and an index
b = "Hello, World!"
print(b[2:5]) # elements from index 2 to 4 (does not include 5)
print(b[:5]) # elements from index 0 to 4 (does not include 5)
print(b[2:]) # elements from index 2 to the last
print(b[:]) # all the elements
print(b[-5:-2]) # elements from index -5 to -3 (does not include -2)
print(b[:-1]) # elements from index 0 to -2 (does not include -1)
print(b[-4:]) # elements from index -4 to -1
# indices can also be applied straight into a string literal
print("Hello, World!"[2:5])






# STRING OPERATORS: + and *
a = "Hello"
b = "World"
c = a + b # plus a+b operator concatenates strings a and b
print(c)
c = a + " " + b + "!"
print(c)
c = 3*a # times n*a operator concatenates string a for n times
print(c)






# ESCAPE CHARACTER: \
# special characters can be inserted into strings with \ operator
txt = "Hello \bWorld!" # backspace
print(txt) 
txt = "Hello\tWorld!" # tab
print(txt)
txt = "Hello\rWorld!" # carriage return
print(txt) 
txt = "Hello\nWorld!" # new line
print(txt) 
txt = "This will insert one \\ (backslash)." # backslash
print(txt) 
txt = "This will NOT insert new line \\n."
print(txt)
txt = 'It\'s alright.' # single quote
print(txt) 
txt = 'It works for \" also.' # double quote
print(txt) 
txt = "\x48\x65\x6c\x6c\x6f" # hexadecimal
print(txt)
txt = "\110\145\154\154\157" # octal
print(txt)
txt = "This is a full block character: \u2588" # unicode characters
print(txt)
# raw strings are not formatted in any way
txt = r"new line \n will not appear" # letter r before the string
print(txt)





# FORMATTING OPERATORS: %, {} and f-strings

# old % operator
txt = "String %s will be replaced." %"with this" # s is format character for strings
print(txt)
name = "John"
age = 23
txt = "%s is %d years old." % (name, age) # s is for strings, d for integers
print(txt)
# txt = "%s is %d years old." % (name, name) # this would create an error
txt = "Hey %(name)s, you are %(age).3f years old!" %{"age": 25,"name": name}
print(txt)
# Python has at least the following format characters:
# %s - Strings (or any object with a string representation, like numbers)
# %d - Integers
# %f - Floating point numbers
# %.<number of digits>f - Float with a given amount of digits

# new {} operator
quantity = 3
itemno = 567
price = 49.95
txt = "I want {} pieces of item {} for {:.1f} dollars."
print(txt.format(quantity, itemno, price))
txt = "I want to pay {2} dollars for {0} pieces of item {1}."
print(txt.format(quantity, itemno, price))
txt = "I have a {carname}, it is a {model}."
print(txt.format(carname = "Ford", model = "Mustang"))

# Formatted string literals = f-strings (from Python 3.6 forwards)
a = 5
b = 10
txt = f"Five plus ten is {a + b} and not {2 * (a + b)}."
print(txt) # f at the beginning does the same thing as format()-function
name = "John"
age = 23
txt = f"Hey {name}, you are {age:.1f} years old!"
print(txt)







# STRING METHODS
# there are a lot of methods for strings, below is just a few of them
# notice that the methods do not change the original string, but return a new one
a = "Hello, World!"
b = a.upper() # every character into upper case
print(b)
c = a.lower() # every character into lower case
print(c)
print(a) # the string a itself is still the original
a = "   Hello, World!   "
d = a.strip() # strips spaces from the beginning and end
print(d) # prints "Hello, World!"
a = "Hello, World!"
e = a.replace("H", "J") # replaces all the H letters with J
print(e) # prints "Jello, World!"
f = a.split(",") # splits the string from the , characters
print(f) # prints ['Hello', ' World!']
f[0]="new string" # f is now a list, and we can change the elements
print(f)
# all the methods can also be applied straight into a string literal
print("word!".upper())
