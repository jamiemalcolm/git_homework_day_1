# I found out how to generate a random number with a google search and tried it
# Failed multiple times trying to run the code with some errors in the elif syntax
import random
# I read some documentation on import and found i needed that to get the code to generate the number
n = random.randint(1, 100)
# still dont understnd it all that well
number = int(input("guess a number from 1 to 100.  "))
while number != n:
  if number < n:
      print("too low! try again")
      number = int(input("guess a number from 1 to 100.  "))
  elif number > n:
    print("too high!, try again")
    number = int(input("guess a number from 1 to 100.  "))
  if number == n:
    print("well done!")
# took some time but eventually managed to get it to output what i wanted.
# 
# I used stack overflow, pythonforbeginners.com and docs.python.org to
# 
# help me get to my solution.    