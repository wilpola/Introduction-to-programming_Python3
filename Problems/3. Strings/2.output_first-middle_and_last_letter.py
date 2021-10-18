import random

def output(word):
  w = word
  f = w[0]
  m = len(w) / 2 # regular division
  # floor division //
  print(f)
  print(w[int(m)])
  print(w[-1])

  
    

words = [ "quick", "letters", "apple", "appreciates", "programming", "zippers", "key", "paragraph", "admin", "student", "teacher", "compare", "dog", "designing", "development", "studies", "run", "dynamic", "fox", "place" ]

for i in range(0,4):
  word = random.choice(words)
  print ("The word is: " + word)
  print ("1st, middle and last letter are:")
  output(word)

