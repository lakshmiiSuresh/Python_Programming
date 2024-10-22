# def function_name(n):#parameters
#     print("success",n)
# function_name(10)#arguments


# def function_name(n):#parameters
#     print("success",n)
# function_name(10,20)#arguments
# #same number of arguments and parameters


# # input 2 numbers from user and call the function . inside function perform addition
# def addition(a,b):
#     print(a+b)
# num1 = int(input("Enter number 1: "))
# num2 = int(input("Enter number 2: "))
# addition(num1,num2)


# def addition(a,b):
#     return a+b
#     # print(a+b) after return if print is given it won't work
# num1 = int(input("Enter number 1: "))
# num2 = int(input("Enter number 2: "))
# print(addition(num1,num2)) #if return is given, then call will be given in print


# #passing list to function
# def function_name(n):
#     print("success",n)
#     for i in n:
#         print(i)
# a = [10,20,30]
# function_name(a)


# #sum of elements in a list
# def list1(n):
#     sum1 = 0
#     for i in n:
#         sum1 = sum1 + i
#     return sum1
# a = [10,20,30]
# print(list1(a))

# #palindrome
# def palindrome(str1):
#     str1 = str1[::-1]
#     if str1 == string1:
#         print("Palindrome")
#     else:
#         print("not palindrome")

# string1 = input("Enter a string: ")
# palindrome(string1)



# # while True:
# #     def cal(ch):
# #         a = int(input("Enter number 1: "))
# #         b = int(input("Enter number 2: "))
# #         if choice == 1:
# #             sum1 = a+b
# #             print(sum1)
# #         elif choice == 2:
# #             diff1 = a-b
# #             print(diff1)
# #         elif choice1 == 3:
# #             mul = a*b
# #             print(mul)
# #         elif choice1 == 4:
# #             div = a/b
# #             print(div)
# #         elif choice1 == 5:
# #             break

# #     choice = int(input("Select your choice: \n1.Addition \n2.Subtraction \n3.Multiplication \n4.Division \n5.Exit"))
# #     cal(choice)


# # calculator
# def add(a,b):
#     sum1 = a+b
#     print(sum1)
        
# def diff(a,b):
#     diff1 = a-b
#     print(diff1)

# def mul(a,b):
#     mul = a*b
#     print(mul)
        
# def div(a,b):
#     div = a/b
#     print(div)

# while True:       
#     choice = int(input("Select your choice: \n1.Addition \n2.Subtraction \n3.Multiplication \n4.Division \n5.Exit"))
#     if choice<5:
#         x = int(input("Enter number 1: "))
#         y = int(input("Enter number 2: "))
#     if choice == 1:
#         add(x,y)     
#     elif choice == 2:
#         diff(x,y)
#     elif choice == 3:
#         mul(x,y)
#     elif choice == 4:
#         div(x,y)
#     else:
#         break
    

# # Registration form 
# dict1 = {}
# def register(un,pw):
#     if un not in dict1.items():
#         dict1.update({un:pw})
#         print("Registration successful!")
#         print(dict1)
#     else:
#         print("Registration unsuccessful")

# def login(un,pw):
#     if un in dict1.keys() and pw in dict1.values():
#         print("Login successful!")
#     else:
#         print("Login unsuccessful")

# while True:
#     choice = int(input("Main Menu: \n1.Register \n2.Login \n3.Exit \nEnter your choice(1/2/3): "))
#     if choice<3:
#         u = input("Enter your username: ")
#         p = input("Enter your password: ")
#     if choice == 1:
#         register(u,p)
#     elif choice == 2:
#         login(u,p)
#     else:
#         break


#function can be called any number of times
# def function_name(name,age=30):
#     print("success",name,age)
# function_name("ammu") 
# function_name("anu",20)
# age is default so only name need to be passed

# def function_name():
#     a = 100
#     print("success")
# function_name()
# print(a)# a is local variable 

# b - global variable
# b = 200
# def function_name():
#     a = 100
#     print(a)
#     print(b)
#     print("success")
# function_name()

# # global a - to make local variable a global
# b = 200
# def function_name():
#     global a
#     a = 100
#     print(a)
#     print(b)
#     print("success")
# function_name()
# print(a)

# #not possible
# # def display(a):
# #     print(a)
# # display(10,20,30)

# # arbitrary arguments - *args
# def display(*a):
#     print(a)
# display(10,20,30)


# def display(a,b,c):
#     print(a,b,c)
# display(a=10,b=20,c=30)

# # keywordargument- **kwargs
# def display(**a):
#     print(a)
# display(a=10,b=20,c=30)

# def display(n):
#     if n==0:
#         return n
#     else:
#         return n + display(n-1)
#     # 5+display(4)
#     # 5+4+display(3)
#     # 5+4+3+display(2)
#     # 5+4+3+2+display(1)
#     # 5+4+3+2+1+display(0)
#     # 5+4+3+2+1+0=15
# print(display(5))

# def factorial(n):
#     if n == 0 :
#         return 1
#     else:
#         return n*factorial(n-1)
# print(factorial(5))

# #sum of digits of a number inputing from user
# def digitsum(a):
#     if a == 0:
#         return 0
#     else:
#         b = a%10
#         a = a//10
#         return b + digitsum(a)
# n = int(input("Enter a number: "))
# print(digitsum(n))

# # write a recursion function to reverse a string
# def reverse(s):
#     if len(s) == 0:
#         return s
#     else:
#         return s[-1] + reverse(s[:-1])
# str1 = input("Enter a string: ")
# print(reverse(str1))


#write a recursion function to calculate x raised to the power n
# def power(a,b):
#     if b == 0:
#         return 1
#     else:
#         return a*power(a,b-1)
# print(power(2,3))

# #1. fibonacci series using recursion.
# def fibonacci(n):
#     a, b = 0, 1
#     while a <= n:
#         print(a, end=" ")
#         a, b = b, a + b

# number = int(input("Enter the maximum number: "))
# fibonacci(number)



# 2. input
#    list1 = ["a","b","c","d","e","f","g","h","i"]
#    list2 = [0,1,1,0,1,2,2,0,1]
#    output - ["a","d","h","b","c","e","i","f","g"]

# wrong
# list1 = ["a","b","c","d","e","f","g","h","i"]
# list2 = [0,1,1,0,1,2,2,0,1]
# list3 = []
# for i in range(len(list1)):
#     for j in range(3):
#         if list2[i] == 0:
#             list3.append(list1[i])
#         elif list2[i] == 1:
#             list3.append(list1[i])
#         elif list2[i] == 2:
#             list3.append(list1[i])
# print(list3)

# #correct
# list1 = ["a","b","c","d","e","f","g","h","i"]
# list2 = [0,1,1,0,1,2,2,0,1]
# list3 = []
# for j in range(3):
#     for i in range(len(list1)):
#         if list2[i] == j:
#             list3.append(list1[i])
# print(list3)

#----------------------------------
# anonymous function - lamda
# lambda arguments:expression
# x = lambda a,b:a+b
# print(x(10,20))

# x = lambda a,b,c:a+b+c
# print(x(10,20,30))

# p = [1,2,3,4,5,6,7,8,9,10]
# # filter(function,itreable)
# x = filter(lambda a:a%2==0,p)#only for even 
# x = list(filter(lambda a:a%2==0,p))
# print(x)

# without lamda .using only normal function
# def display(n):
#     return n%2==0
# p = [1,2,3,4,5,6,7,8,9,10] 
# x = list(filter(display,p))  
# print(x,"output")

# p = [1,2,3,4,5,6,7,8,9,10]
# x=list(map(lambda a:a**2,p))#map for doing every element
# print(x)

# from functools import reduce # reduce - to get single value
# p = [1,2,3,4,5,6,7,8,9,10]
# x = reduce(lambda a,b:a+b,p) # a will get the sum and b will get the iterable
#                 #  1,2:3     
#                 #  3,3:6
#                 #  6,4:10
# print(x)

# 1.find the positive numbers
# p=[1,-1,2,-2,3,-3]
# x = list(filter(lambda a:a>0,p))
# print(x)

# without lambda
# def positive(n):
#         if n>0:
#             return n
# p=[1,-1,2,-2,3,-3]
# x = list(filter(positive,p))
# print(x)

# 2.find the strings which are palindrome
# k=["mom","level","bat","cat"]
# x = list(filter(lambda a:a[::-1]==a,k))
# print(x)


# # 3.convert each string to capital letters
# t=["hello","python","hai","java"]
# x = list(map(lambda a:a.upper(),t))
# print(x)

# without lambda
# def capital(n):


# # 4.calculate length of each string
# y = ["apple","banana","pineapple","mango"]
# x = list(map(lambda a:len(a),y))
# print(x)

# # 5.find the maximum value
# from functools import reduce 
# e = [3,5,6,8,1]
# x = reduce(lambda a,b:max(a,b),e)
# print(x)

# 6.concatenate them into a single string
# from functools import reduce
# h = ["hello","python","programming","language"]
# x = reduce(lambda a,b:a+" "+b,h)
# print(x)

# 7.write a lambda function to add 10 to a given number
# x = lambda a:a+10
# print(x(5))


# def display(a):
#     return a
# x = lambda a:display(a) #lambda calling function instead of expression
# print(x(10))


# def show(n):
#     return n%2==0
# p = [1,2,3,4,5,6,7,8,9,10]
# x = list(filter(lambda a: show(a),p))# lamda inside filter calling function
# print(x)


# def outer_function():
#     def inner_function():
#         return "inner function"
#     return "outer function" #only outer function return runs since only calling outer function

# print(outer_function())


# def outer_function():
#     def inner_function():
#         return "inner function"
#     return inner_function()
# print(outer_function())

# 1.from a list of numbers remove zero to the end of the list
# list1 = [1,0,2,0,4,6]
# for i in list1:
#     if i==0:
#         list1.remove(i)
#         list1.append(i)
# print(list1)


# # 2.write a python function that takes a list and returns a  
# # new list with distinct elements from the list 
# def distinct(l1):
#     l2 = []
#     for i in l1:
#         if i not in l2:
#             l2.append(i)
#     print(l2)
# list1 = [1,2,3,3,3,3,4,5]
# distinct(list1)
# make list to set

# 3.find the missing number
# list1 = [1,2,4,5,6]
# for i in range(len(list1)):
#     if list1[i]!=i+1:
#         print(i+1)
#         break
       
list1 = [1,2,4,5,6]
for i in list1:
    if i!=(i+1)-i:
        print("Missing number:",i+1)
        break   

def display(l):
    n = len(l)+1
    total = n*(n+1)//2
    total_l=sum(l)
    missing_num = total-total_l
    return missing_num
list1 = [1,2,4,5,6]
print(display(list1))

# 1.What is the python program to find pairs of numbers from a given list such that the 
# sum  of their squares equals a perfect square
# a^2 +b^2 = c^2
# input : a= [1,2,3,4,5,6,7,8,9,10]
# output: 3,4 ,5
        #   6,8,10

l = [1,2,3,4,5,6,7,8,9,10]
for i in range(len(l)):
    for j in range(1,len(l)):
        for k in range(2,len(l)):
            x = l[i]**2
            y = l[j]**2
            z = l[k]**2
            if x+y == z:
                # print(l[i])
                # print(l[j])
                # print(l[k])
                print(i+1,j+1,k+1)

l = [1,2,3,4,5,6,7,8,9,10]
for i in l:
    for j in l:
        for k in l:
            x = l[i]**2
            y = l[j]**2
            z = l[k]**2
            if x+y == z:
                print(l[i])
                print(l[j])
                print(l[k])
                # print(i+1,j+1,k+1)


# sorted method
# syntax: sorted(iterable,key=none,reverse=True)
l=[10,12,81,54,60]
print(sorted(l))#to sort the list

l=[10,12,81,54,60]
print(sorted(l,reverse=True))

l=["abc","python","apple","bat","java"]
print(sorted(l,key=len))#sorted based on alphabet and length

# reversed
l=[10,12,81,54,60]
print(list(reversed(l)))#to reverse the list

for i in reversed(range(5)):#can reverse the range
    print(i)

f = "hello"
x = "".join(reversed(f))#join after reversed
y = list((reversed(f)))
print(x)
print(y)
# str - list === split

# enumerate
l = [10,20,30,40,50,60,70]
for i,j in enumerate(l):
    print(i,j) 

l = [10,20,30,40,50,60,70]
for i,j in enumerate(l,start=1):
    print(i,j) 

