import random
def middle_or_none(w):
    if len(w) % 2 == 0:
        return("none")
    else:
        return (w[int(len(w) / 2)])


words = [ "rare", "letters", "feta", "appreciates", "programming", "programmer", "key", "paragraph", "automate", "student", "lame", "compare", "evaluate", "designing", "development", "call", "define", "dynamic", "snap", "place" ]

for i in range(0, 4):
  w = random.choice(words)
  print ("The word is: " + w)
  print ("Middle letter is: ", middle_or_none(w))