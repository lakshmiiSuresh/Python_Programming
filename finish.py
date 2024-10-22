
# s1 = "hello"
# s2 = "world"
# l=[]
# r = s1[:6:2]
# s = s2[:6:2]
# print(r+s)

# S1 = "hello"
# S2 = "world"
# l=[]
# new_String = "hwlrod"
# p=len(S1)
# for i in range(len(S1)):
#     for j in range(len(S2)):
#         if i%2 == 0 and j%2==0:
#             l.append(S1[i]+S2[j])
#         break
# print(l)


S1 = "hello"
S2 = "world"
new_String = ""
p = len(S1)
for i in range(p+1):
    if i % 2 == 0:
        new_String += S1[i]
    else:
        new_String += S2[i-1]
print(new_String)



l = [1, 3, 2, 3]
s = set(l)
m=1
for i in s:
    m = m * i
print(m)


# 3.write a program that counts the number of strings that have a length greater 
# than 2 and start and end with the same character

s = ["aea","abbbaeea"]
for i in s:
    if len(i) and i[0]==i[-1]:
        print(i,end=" ")


# write a program to remove the characters which have odd index values of a given string.
s = "aeeeea"
l=[]
for i in range(len(s)):
    if i%2==0:
        l.append(s[i]) 
        print("".join(l))  
print("".join(l))     


s = [0,1,2,3,4,5]
l = []
# len(s)=6
for i in range(0,len(s)-1,2):
        l.append(s[i+1])
        l.append(s[i])
print(l)


# write a python program to print length of unique characters in a string.
p = "aaabccc"
s=""
for i in p:
    if i not in s:
        s = s+i
print(len(s))

# Write a python program to convert a tuple to a string.
t = ("aa",1,2)
s = str(t)
print(s)

# 8.write a python program to seperate positive and negative number from a list.
l=[0,1,-2,3,-5,2]
pl=[]
nl=[]
for i in l:
    if i>=0:
        pl.append(i)
    else:
        nl.append(i)
print("positive list:",pl)
print("negativelist:",nl)


# 9. anagrams count printing in dictionary
import random
words = ['eat','tea','ten','bat','ate','net','dub','bud']
dict1 = {}
count = 0
anagram_dict = {}
for word in words:
    word_list = list(word)
    print(word_list)
    random.shuffle(word_list)
#     for j in i:
#         s = random.shuffle(j)
#         if s in words:
#             count+=1
# dict1[s]=count
# print(dict1)

        



