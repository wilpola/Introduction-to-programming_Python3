# @author: Ville Wilpola
# @date: 2021-10-29
# Score: 10/10

import random


def output_vowels(s):
    # print(" ")
    for char in s:
        if char in 'aeiouy':
            print(char)

chars = "abcdeiforusy"
string = ""
for i in range(0,24):
  string += random.choice(chars)

print ("The string is: " + string)
print ("Vowels:")
output_vowels(string)