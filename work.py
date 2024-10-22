# # variable declaration
# a = 12
# b = 'c'
# c = 12.5
# # d = 
# e = True
# print(a)


# print("Hello World")

# a = 10
# b = 12
# s = a+b
# d = a-b
# c = a**3
# print(pow(a,3))
# print(s)
# print(d)
# print(c)


# # without temp
# a = 10
# b = 20
# print("Before swapping:")
# print("a = ",a)
# print("b = ",b)
# a = a+b
# b = a-b
# a = a-b
# print("After swapping:")
# print("a = ",a)
# print("b = ",b)

# # using temp
# a = 10
# b = 20
# temp = a
# a = b
# b = temp
# print("a = ",a)
# print("b = ",b)


# n = 5
# fact = 1
# for i in range(1,6):
#     fact = fact*i
# print(fact)

# ----------------------------------
# a = int(input("Enter first number"))
# b = int(input("Enter second number"))
# if a>b:
#     print(a,"is greater")
# else:
#     print(b,'is greater')


# a = 10000
# b = 300
# c = 40
# if a>b and a>c:
#     print(a," is greater")
# elif b>a and b>c:
#     print(b," is greater")
# else:
#     print(c,"is greater")


# a = int(input("Enter a number"))
# if a%2 == 0:
#     print(a,"is an even number")
# else:
#     print(a,"is not even")

# if a%2 != 0:
#     print(a,"is odd")
# else:
#     print(a,"is not odd")


# a = int(input("Enter a number: "))
# if a%2==0:
#     if a%5==0:
#         print("divisible by both 2 and 5")
#     else:
#         print("Divisible by 2 but not by 5")
# else:
#     if a%5==0:
#         print("divisible by 5 but not by 2")
#     else:
#         print("not divisible by 2 nor 5")
        

# a = 153
# n = str(a)
# l = len(n)
# am = 0
# x = a
# while x > 0:
#     i = x%10
#     x = x//10
#     # r = r * 10 + i
#     am = am + i**l
# print(am)
# if am == a:
#     print("Amstrong")
# else:
#     print("not amstrong")

# ------------------------------

# n = int(input("Enter a number: "))
# rev = 0
# a = n
# while a>0:
#     i = a%10
#     a = a//10
#     rev = rev * 10 + i
# print(rev)
# if rev == n:
#     print("Palindrome")
# else:
#     print("Not palindrome")


# n = int(input("Enter a number: "))
# for i in range(2,n):
#     if n%i==0:

# Program to check if a number is prime or not

num = 2

# To take input from the user
#num = int(input("Enter a number: "))

# define a flag variable
# flag = False

# if num == 0 or num == 1:
#     print(num, "is not a prime number")
# elif num > 1:
#     # check for factors
#     for i in range(2, num):
#         if (num % i) == 0:
#             # if factor is found, set flag to True
#             flag = True
#             # break out of loop
#             break
#     # check if flag is True
#     if flag:
#         print(num, "is not a prime number")
#     else:
#         print(num, "is a prime number")


# n = int(input("Enter a number: "))
# rev = 0
# a = n
# while a>0:
#     i = a%10
#     a = a//10
#     rev = rev * 10 + i
# print(rev)


s = "hai hello how are you"
t = "hello are"
s1 = s.split(" ")
t1 = t.split(" ")
l1 = []
for i in s1:
    if i not in t1:
            l1.append(i)
print(l1)

s = "hai hello how are you"
t = "hello are"
s1 = s.split(" ")
t1 = t.split(" ")

l1 = [i for i in s1 if i not in t1]
print(l1)


s = "hai hello how are you"
t = "hello are"
s1 = s.split(" ")
t1 = t.split(" ")
l1 = []
for i in s1:
    for j in t1:
        if i not in l1 and i==j:
            break
    else:
        l1.append(i)
print(l1)


s = "hai hello how are you"
t = "hello are"
s1 = s.split(" ")
t1 = t.split(" ")
l1 = []
for i in s1:
    for j in t1:
        if i not in l1 and i==j:
            break
    else:
        l1.append(i)
print(l1)

print(dir(str))

x=0
for i in range(100000):
        x+=1
print(x)


# ---------------------------------- question paper----------------------
def sum(l):
    if len(l)==0:
        return 0
    return l[0]+sum(l[1:])
  
l1 = [1,2,3,4,5]
print(sum(l1))

class Person:
    def __init__(self,a,b):
        self.a=a
        self.b=b

class Student(Person):
    def display(self):
        print("Name: ",self.a)


s = Student("laks",1)
