
#triangle checking
# angle1 = int(input("Enter first angle: "))
# angle2 = int(input("Enter second angle: "))
# angle3 = int(input("Enter third angle :"))
# sumt = angle1+angle2+angle3
# if sumt==180:
#     print("It is a triangle")
# else:
#     print("Not a triangle")

# price = int(input("Enter the amount you have purchased: "))
# if price>=10000:
#     print("You have got a 10% discount")
# else:
#     print("No discount")


#reverse of a number
# num = 675
# rev = 0
# while num>0:
#     i=num%10
#     num = num//10
#     rev = rev * 10 + i
# print(rev)


#palindrome of number
# num = 675
# rev = 0
# while num>0:
#     i=num%10
#     num = num//10
#     rev = rev * 10 + i
# print(rev)
# if num == rev:
#     print("palindrome")
# else:
#     print("Not palindrome")

#prime using while loop
# n = 2
# i = 2
# f = 0
# while n>0:
#     if n%i==0:
#         f=1
#         break
#     i+=1
# if f==0:
#     print("prime")
# else:
#     print("not prime")

#amstrong
num1 = int(input("Enter a number: "))
x = num1
p = len(str(num1))
ams = 0
while x>0:
    i = x%10
    x = x//10
    ams =  ams + i**p
# print(ams)
print(num1)
if num1 == ams:
    print("Amstrong")
else:
    print("Not amstrong")

#swap without temp var
a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
#using temp c
# c = a
# a = b
# b = c
if a != b:
    a = a+b
    b = a-b
    a = a-b
else:
    print("a and b are same")
print("Numbers after swaping: ")
print("First number: ",a)
print("Second number: ",b)

#.................................................

# forloop
# for i in range(1,11):
#     print(i)


# s = 0
# for i in range(1,11):
#     s = s + i
# print("Sum is :",s)


# for i in range(2,21,2):
#     print(i)


# for i in range(1,21,2):
#     print(i)


# for i in range(20,0,-2):
#     print(i)
    

#factorial of a number
# n = int(input("Enter a number: "))
# if n<0:
#     print("Enter positive number")
# elif n==0:
#     print("Factorial is 1")
# else:
#     fact = 1
#     for i in range(1,n+1):
#         fact = fact * i 
# print(fact)


#break in forloop
# for i in range(11):
#     if i == 3:
#         break
#     print(i)

# #continue
# for i in range(11):
#     if i==3 or i ==4:
#         continue
#     print(i)



