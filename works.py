# 1. Given a string s, find the length of the longest substring without repeating characters.
str1 = input("Enter a string: ")
l1 = []
a =''
for ch in str1:
    if ch not in a:
        a = a+ch
        l1.append(a)
length=0
b=''
for i in l1:
    if len(i) > length:
        length=len(i)
        b=i
print(b)

# str1 = input("Enter a string: ")
# l1 = []
# for i in range(len(str1)):
#     for j in range(1,len(str1)):
#         if str1[i]!=str1[j]:
#             a=''
#             a=a+str1[i]+str1[j]
#         else:
#             break
# print(l1)


# 2. Given a string s consisting of words and spaces, return the length of the last word in the string.
s = input("Enter a sentence: ")
l = s.split()
print(len(l[-1]))


# 3.Given a sorted array of distinct integers and a target value, 
# return the index if the target is found. If not, return 
# the index where it would be if it were inserted in order.
l1 = [1,3,5,6]
target = 2
for i in l1:
    if i==target:
        print(l1.index(i))
        break
    elif i==target-1:
        c=l1.index(i)
        l1.insert(c+1,target)
        print(l1.index(target))
        break
    elif target>l1[-1]:
            l1.insert(l1[-1],target)
            print(l1.index(target))
            break


# l=[1,3,5,6]
# target=int(input('enter value'))

# if target in l:
#         print(l.index(target))

# else:
#     for i in range(0,len(l)-1):
#         if target>l[i] and target<l[i+1]:
#             l.insert(i+1,target)
#         elif target>l[-1]:
#             l.insert(l[-1],target)
# print(l)


# write a program to find ascii value of a given letter



# WCI is calculated from the wind speed v in miles per hour and the temp t in fahrenheit.
t = float(input("Enter the temparature: "))
v = float(input("Enter the wind speed in miles per hour: "))
if 0<=v<=4:
    wci = t
elif v>=45:
    wci=1.6*t-55
else:
    wci=91.4+(91.4-t)(0.0203*v-0.304)*v/2-0.474

print("wind chill index:",wci)


