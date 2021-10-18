import random

def first_upper(word):
    _ret = word[0].upper() + word[1:].lower()
    _lobs = word.capitalize()
    print(word.capitalize())
    

    print("Returns " + _ret)
    print("Return _lobs: " + _lobs)


words = [ "quick", "letters", "apple", "appreciates", "programming", "zippers", "key", "paragraph", "admin", "student", "teacher", "compare", "dog", "designing", "development", "studies", "run", "dynamic", "fox", "place" ]

for i in range(0,4):
  word = random.choice(words)
  print ("The word is: " + word)
  print ("1st, middle and last letter are:")
  first_upper(word)