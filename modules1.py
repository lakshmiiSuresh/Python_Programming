# 3 ways of importing math module
import math
print(math.factorial(5))
print(math.sqrt(25))

from math import factorial,sqrt
print(factorial(5))
print(sqrt(25))

from math import *
print(factorial(5))
print(sqrt(25))
print(ceil(1.9))
print(ceil(1.1))
print(floor(1.9))
print(floor(1.1))
print(pow(2,5)) #float value [pow in math module]

import math
print(dir(math))

#----------------------------------

print(pow(2,5)) #built-in pow gives integer output.whereas pow in math module gives integer value

#----------------------------------
#random module
import random
l = [1,2,3,4,5]
random.shuffle(l)#for shuffling list
print(l)

print(random.choice(l))#choose random value from list
print(random.random())#choose random value between 0 & 1
print(random.randint(1,10))#random value from the range given i.e b/w 1  & 10.10 is also included
print(random.randrange(1,10,3))#here 3 is skip value so the list will contain [1,4,7] and a random value from this list will be printed. 10 is exluded from range
print(random.sample(l,3))# random 3 values from list will be printed since 3 is given
print(random.sample(l,4))#4 values from list l 


#generate 100 lottery tickets and choose 2 as winners
import random
list1 = []
for i in range(101):
    x = random.randint(100000,999999)
    print(x)
    list1.append(x)
print(random.sample(list1,2))
    

#3 numbers b/w 100 and 999 which is divisible by 5
import random
l = []
for i in range(100,1000):
    l.append(i) 
for x in l: 
    if x%5==0:
        break
print(random.sample(l,3))

for i in range(3):
    print(random.randrange(100,999,5,end=""))


import random
x = random.randint(1,10)
print(x)
for i in range(1,4):
    num = int(input("Guess any number: "))
    if num == x:
        print("You win!!")
        break
    else:
        if i==3:
            print("Game over!")
        else:
            print("You lose.Try again")

    # elif num!=x and i==2:
    #     print("Try again! 1 more chance")
    # elif num!=x and i==3:
    #     print("You loose")
    

import random  
player1 = random.randint(1,6)
player2 = random.randint(1,6)
if player1>player2:
    print("Player1 wins")
elif player1<player2:
    print("Player2 wins")
else: 
    print("It's a tie")

# write a python program that takes a list of words and groups words with
# the same letters into sublists. store all these sublists in a main list and print the result. 
# for example, if the input is ['eat','tea','ten','bat','ate','net'], the program should group 
# anagrams and print the result as a list of lists.
# input : a = ["eat","tea","ate","ten","net","bat"]
# output: b = [["eat","tea","ate"],["net","ten"],["bat"]]

words_main = []
lim = int(input("Enter the number of words: "))
for i in range(lim):
    word = input("Enter word:")
    words_main.append(word)
# print(words_main)
words_main.sort()
print(words_main) 
length = len(words_main)
for i in range(length):
    for j in range(i+1,length):
        sorted(words_main[j])
#---------------------------------
#datetime module
import datetime
x = datetime.datetime.now()
print(x)
print(x.day)
print(x.month)
print(x.year)
print(x.hour)
print(x.minute)
print(x.second)
print(x.microsecond)
print(x.date())#show date as yyyy-mm-dd
print(x.time())#show time only

print(x.strftime("%b"))#month in string as short form
print(x.strftime("%B"))#month in string
print(x.strftime("%y"))#24
print(x.strftime("%Y"))#2024
print(x.strftime("%d"))#date as 21
print(x.strftime("%a"))#day in string as short form
print(x.strftime("%A"))#day in string
print(x.strftime("%w"))#3rd day from sunday
print(x.strftime("%m"))#8th month

