#!/usr/bin/env python
# coding: utf-8

# In[5]:


import math
from random import randint

Guess_game = True
count= 0
limit=3
Score1=0

while Guess_game:
    y = randint(0,10)
    guess = int (input("Enter a number: \n"))
    count +=1
    if guess == y:
        print ("Your guess is right")
    else:
        print ("Try again")
        print ("\n")

#     cont = input("Continue? yes/no:")
#     if cont== "no":
    if count == limit:
        Guess_game = False
        print ("You are out of chances")
#         break
    if guess == y:
        Score1= Score1 + 1
        print ("Your score is" + "\n" + str(Score1))
#     else:
#         print (("Your score is" , str(Score1))
print ("\n")

print ("Round 2")

Guess2= True
count1=0
limit1=3
Score2 = 0

while Guess2:
    y = randint(0,10)
    guess = int (input("Enter a number: \n"))
    count1 +=1
    if guess == y:
        print ("Your guess is right")
#         break
    else:
        print ("Try again")
        print ("\n")

#     cont = input("Continue? yes/no:")
#     if cont== "no":
    if count1 == limit1:
        Guess2 = False
        print ("You are out of chances")
#         break
    if guess == y:
        Score2= Score2 + 1
        print ("Your score is" + "\n" + str(Score2))
#     else:
#         print ("Your score is" + "" + str(Score2))
        
print ("Thanks")


# In[ ]:




