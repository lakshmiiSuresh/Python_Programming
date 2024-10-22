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

# a = int(input("Enter a number: "))
# if a%3 == 0:
#     if a%5 == 0:
#         print(a,"is divisible by 5 and 3")
#     else:
#         print(a,"is divisible by 3 but not by 5")
# else:
#     if a%5 ==0:
#         print(a,"is divisible by 5 but not by 3")
#     else:
#         print(a,"is not divisible by 3 and 5")


# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# s = a+b
# print(s,"is the sum of",a ,"and",b)

# diff = a-b
# print(diff,"is the difference b/w ",a,"and",b)

# a = int(input("Enter a number: "))
# cube = a**3
# print(cube,"is the cube of",a)


# a = int(input("Enter a number"))
# if a%2 == 0:
#     print(a,"is an even number")
# else:
#     print(a,"is not even")

# a = int(input('Enter  number: '))
# if a%2 == 0:
#     print(a,"is not odd")
# else:
#     print(a,"is odd")


# if a%2 != 0:
#     print(a,"is odd")
# else:
#     print(a,"is not odd")


# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# op = input("choose an operator (+,-,*,/)")
# if op == '+':
#     s = a + b
#     print(s,'is the sum of',a ,"and",b)
# elif op == '-':
#     diff = a-b
#     print(diff,'is the difference b/w',a ,"and",b)
# elif op == '*':
#     mul = a*b
#     print(mul,"is",a,"*",b)
# elif op == '/':
#     div = a/b
#     print(div,"is",a,"/",b)




#Leap year
# year = int(input("Enter a year"))
# if year%100==0:
#     if year%400==0:
#         print(year,"is a Leap year")
#     else:
#         print(year,"is not a leap year")
# else:
#     if year%4==0:
#         print(year,"is leap year")
#     else:
#         print(year,"is a not leap year")

# if year%100==0 and year%400 ==0:
#     print("leap year")
# elif year%100!=0 and year%4==0:
#     print("leap year")
# else:
#     print("Not leap year")


# age = int(input("Enter age: "))
# if age>= 18:
#     print("Eligible for voting")
# else:
#     print("Not eligible")

# a = int(input("Enter a number: "))
# if a>0:
#     print("positive number")
# elif a<0:
#     print("Negative number")
# else:
#     print("number is zero")

# i=0
# while i<10:
#     i+=1
#     if i==4:
#         continue
#     print(i)


# i=0
# while i<10:
#     i+=1
#     if i==4:
#         break
#     print(i) 

# i=0
# while i<10:
#     if i==4:
#         break
#     i+=1
#     print(i) 

#sum of 1st 10 natural numbers
i=0
s=0
while i<10:
    i+=1
    s = s+i
print("sum is:",s)    

#sum of cube of 1st 10 natural numbers
i=0
c=0
while i<10:
    i+=1
    c=c+i**3
print(c,"is the sum of cube's")

#reverse of a number
num = 675
rev = ""
while num>0:
    i=num%10
    num = num//10
    rev = rev + str(i)
print(rev)

#palindrome
# str1 = 'malayalam'
# str2 = ''
# p = ''
# length = len(str1)
# while length!=0:
#     str2 = str1[length-1]
#     length-=1
#     p = p + str2
# print(p)
# if str1==p:
#     print("palindrome")   
# else:
#     print("Not palindrome") 


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

# reverse and palindrome of number
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

#prime
n = int(input('enter number : '))
i = 2
f = 0
while i<n:
    if n%i==0:
        f=1
        break
    else:
        f=0
    i+=1
if f==0:
    print("prime")
else:
    print("not prime")

#amstrong or narcissistic number
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
# c = a
# a = b
# b = c
if a != b:
    a = a+b
    b = a-b
    a = a-b
else:
    print("A and b are same")
print("Numbers after swaping: ")
print("First number: ",a)
print("Second number: ",b)








