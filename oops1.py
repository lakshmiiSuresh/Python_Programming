# class Classname:
#     pass
# objectname = Classname()

# class Bird:
#     eyes = 2 
#     beak = 1
#     def fly(self):#method inside class should have self parameter
#         print("parrot")

# parrot = Bird()
# print(parrot.eyes)
# print(parrot.beak)
# peacock=Bird()
# print(peacock.eyes)
# print(peacock.beak)
# # one plan can be used to build many house similarly 
# # one class can have many objects

# parrot.eyes = 1
# print(parrot.eyes,"eyes")#parrot eyes changes
# print(peacock.eyes)#peacock eyes no change

# parrot.fly()#caling fly method



# class Bird:
#     eyes = 2
#     beak = 1
#     def fly(self,a):
#         print(a)

# parrot=Bird()
# peacock=Bird()
# parrot.fly("parrot")#passing argument to a
# peacock.fly("peacock")#passing to a



# class Bird:
#     eyes = 2
#     beak = 1
#     def fly(self,a):
#         self.a=a
#         print(a)
#     def walk(self):
#         print(self.a)

# parrot = Bird()
# peacock=Bird()
# parrot.fly("parrot")
# peacock.fly("peacock")
# parrot.walk()

# class Sum:
#     def inputs(self):
#         a = int(input("Enter number1: "))
#         self.a = a
#         b = int(input("Enter number2: "))
#         self.b = b
#     def addition(self):
#         sum = self.a+self.b
#         self.sum = sum
#     def result(self):
#         res = self.sum
#         print(res)

# add = Sum()
# add.inputs()
# add.addition()
# add.result()


# Class Addition:
#     def num(self):
#         self.a = a
#         self.b = b
#     def calculation:
#         self.c = self.a +self.b
#     def result(self):
#         print(self.c)

# add = Addition()
# add.inputs(100,200)
# add.calculation()
# add.result()
# to change the values of a and b 
# add.a = 400
# add.b = 500
# add.calculation()
# add.result()

# class Rectangle:
#     def inputs(self,l,b):
#         self.l = l
#         self.b = b
#     def area(self):
#         self.area = self.l*self.b
#         print(self.area)
#     def p(self):
#         self.p = 2*(self.l+self.b)
#         print(self.p)

# r = Rectangle()
# r.inputs(10,5)
# r.area()
# r.p()


# class Book:
#     def title(self,t):
#         self.t = t
#     def author(self,a):
#         self.a = a
#     def display(self):
#         print(self.t,"-Title")
#         print(self.a," -Author")

# b = Book()
# b.title("Alchemist")
# b.author("Paulo coelho")
# b.display()


class Bank:
    def initial(self,a):
        self.a= a
        print(self.a)
    def deposit(self,d):
        self.d=d
        self.a+=self.d
    def withdraw(self,w):
        self.w=w
        self.a-=self.w
    def balance(self):
        print("Current balance:",self.a)
b = Bank()
while True:
    ch = int(input("Select: \n1.Add Details \n2.Deposit \n3.Withdraw \n4.Current Balance \n5.Exit  \nEnter your choice: "))
    if ch==1:
        name = input("Enter your name: ")
        acc_no = input("Enter your account number: ")
        initial_amount = int(input("Enter initial amount: "))
        b.initial(initial_amount)
    elif ch==2:
        depo = int(input("Enter the amount to be deposited: "))
        b.deposit(depo)
        b.balance()
    elif ch==3:
        withd = int(input("Enter the amount to be withdrawn: "))
        b.withdraw(withd)
        b.balance()
    elif ch==4:
        b.balance()
    elif ch==5:
        break

# ---------------------------------------------------------

# constructor - class inu object create cheyambo invoke cheyunna method
# values object inte oppam pass cheymm
class Student:
    college = "abc"
    def __init__(self,a):
        print("welcome",a)
    def study(self):
        print("studying")

ammu=Student(1000)
# print(ammu.college)
# ammu.study()

# create a class person that initialises 
# with a name and age include a 
# method display info that prints the name and age of person

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display_info(self):
        print("Name",self.name)
        print("Age",self.age)

p = Person("laks",20)#values passed when object is created
p.display_info()


# Find area using constructor
class Rectangle:
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def area(self):
        self.a = self.l*self.b
        print("Area",self.a)

rect = Rectangle(20,10)#values are passed when object is created
rect.area()

# create a class student that initialises with a name and a list of grades 
# write methods to calculate the avg grade an display the students details

class Student:
    def __init__(self,name,gl):
        self.name=name
        self.gl = gl
    def avg_grade(self):
        self.g = sum(self.gl)/len(self.gl)
    def display(self):
        print("Student Details:")
        print("Name:",self.name)
        print("Grades:",self.gl)
        print("Average grade",self.g)
        
s = Student("laks",[90,85,90,90])
s.avg_grade()
s.display()


# ----------------------------------------------------------------------

# Inheritance
# single inheritance
class Father:
    def __init__(self):
        print("Father page")
    def phone(self):
        print("phone is using")
    def walk(self):
        print("Walking")
class Son(Father):
    def __init__(self):
        print("son page")
    def study(self):
        print("Studying")

f=Son()#object of son is created for inheritance
f.phone()
f.walk()
f.study()
# if there is constructor for both parent & child, then constructr of child will display 
# if there is no constructor for child but parent have constructor,then parent construct will display

#-------------------------------------
class Father:
    def __init__(self):
        print("Father page")
    def phone(self):
        print("phone is using")
    def walk(self):
        print("Walking")
class Son(Father):
    def __init__(self):
        print("son page")
        super().__init__()#super method
        Father.__init__(self)#to invoke parent method
    def study(self):
        print("Studying")
# if both child and parent are having constructor,by default child constructor will be displayed
# so to display parent constructor use super method or by invoking parent method
f=Son()#object of son is created for inheritance
f.phone()
f.walk()
f.study()

# parametrised 
class Son:
    def __init__(self,a,b):
        print("phone is using")
f=Son(10,20)

#non parameterised
class Son:
    def __init__(self):
        print("phone is using")
f=Son()

# copy constructor

# --------------------------------------------------------
# multi level inheritance
class Grandfather:
    def phone(self):
        print("phone is using")
class Father(Grandfather):
    def walk(self):
        print("walking")
class Son(Father):
    def study(self):
        print("studying")
f=Son()
f.study()#study method in son class
f.phone()#phone method not in son class.so it will check its parent class Father and phone method is not there also.so it will check fathers parent grandfather and there is phone method
f.walk()#walk method not in son.so it will check its parent father and it have walk method 

# -----------------------------------------------------------
# multiple inheritance -#2 parent 1 child
class Father:
    def phone(self):
        print("phone is using")
class Mother:
    def walk(self):
        print("walking")
class Son(Mother,Father):
    def study(self):
        print("studying")
f=Son()
f.study()
f.phone()
f.walk()

# phone method in both parents.Since class Son(Mother,Father) Mother is first 
# it will be printing mothers method
class Father:
    def phone(self):
        print("Father class")
class Mother:
    def phone(self):
        print("Mother class")
class Son(Mother,Father):
    def study(self):
        print("studying")
f=Son()
f.study()
f.phone()#mothers phone method. since son first inherits from mother parent

class Father:
    def phone(self):
        print("Father class")
class Mother:
    def phone(self):
        print("Mother class")
class Son(Father,Mother):
    def study(self):
        print("studying")
f=Son()
f.study()
f.phone()#father class's phon method since son first inherits from father class then mother class

# ----------------------------------------------------
# heirarchical inheritance
# One parent and two child .no relationships between children
class Vehicle:
    def acceleration(self):
        print("Vehicle class")
class Car(Vehicle):
    def four(self):
        print("four wheeler")
class Bike(Vehicle):
    def two(self):
        print("two wheeler")

f=Car()
f.four()
f.acceleration()
# f.two()#car have no relationship with bike
ff=Bike()
ff.acceleration()
ff.two()
# ff.four()#bike have no relation with car

# --------------------------------------------------
#hybrid inheritance
class Grandfather:
    def phone(self):
        print("phone is using")
class Father(Grandfather):
    def walk(self):
        print("walking")
class Mother(Grandfather):
    def phone(self):
        print("walking")
class Son(Father,Mother):
    def study(self):
        print("studying")

f=Son()
f.study()
f.phone()
f.walk()
f.climb()


class School:
    def fun1(self):
        print("School class")
class Teacher1(School):
    def fun2(self):
        print("Teacher1 class")
class Teacher2(School):
    def fun3(self):
        print("Teacher1 class")
class Student(Teacher1,Teacher2):
    def fun4(self):
        print("student class")
object6=Student()
object6.fun4()
object6.fun3()
object6.fun2()
object6.fun1()
print(Student.__mro__)#method resolution order



class Grandfather:
    def __init__(self,g):
        print("Grandfather class:",g)
class Father(Grandfather):
    def __init__(self,f,g):
        print("father class:",f,g)
        super().__init__(g)
class Son(Father):
    def __init__(self,s,f,g):
        print("Son class:",s,f,g)
        super().__init__(f,g)
f=Son("son","father","grandfather")
