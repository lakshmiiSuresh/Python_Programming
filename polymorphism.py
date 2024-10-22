# overloading is not supported in python
# method overloading -python does not support
# constructor overloading -python does not support
# operator overloading is supported in python

# method overloading
# example:
# class Student have 2 methods.since both methods have same name .2nd method runs
# this is because 1st method gets overwritten by second method
# same class ,same method,diff number of parameters
# class Student:
#     def display(self,a,b):
#         print(a+b)

#     def display(self,a,b,c):
#         print(a+b+c)

# s = Student()
# s.display(10,20,30)
# s.display(10,20) #error because python is interpreted so 1st display is replaced by 2nd

# # constructor overloading
# class Student:
#     def __init__(self,a,b):
#         print(a+b)
    
#     def __init__(self,a,b,c):
#         print(a+b+c)

# s=Student(10,20) #TypeError: Student.__init__() missing 1 required positional argument: 'c'


# # operator overloading 
# # magic methods/dunder methods is used in operators between objects
# class Student:
#     def __init__(self,a):
#         self.a=a
#         # print(a)

#     def __add__(self,other):
#         print(self.a)#first object
#         print(other.a)#second object
#         print(self.a+other.a)

# s=Student(10)
# ss=Student(20)
# s+ss #for to add object __add__(self,other) is needed

# # s-ss  s.__sub__(ss)
# # s*ss  s.__mul__(ss)
# # s**ss  s.__pow__(ss)
# # s/ss  s.__truediv__(ss)
# # s//ss  s.__floordiv__(ss)
# # s%ss  s.__mod__(ss)

# # sub
# class Student:
#     def __init__(self,a):
#         self.a=a
#         # print(a)

#     def __sub__(self,other):
#         print(self.a)#first object
#         print(other.a)#second object
#         print(self.a-other.a)

# s=Student(10)
# ss=Student(20)
# s-ss

# comparison operators
# p1<p2  p1.__lt__(p2)
# p1<=p2 p1.__le__(p2)
# p1==p2 p1.__eq__(p2)
# p1!=p2 p1.__ne__(p2)
# p1>p2  p1.__gt__(p2)
# p1>=p2 p1.__ge__(p2)

# class Student:
#     def __init__(self,a):
#         self.a=a
#         # print(a)

#     def __gt__(self,other):
#         print(self.a)#first object
#         print(other.a)#second object
#         print(self.a>other.a)

# s=Student(10)
# ss=Student(20)
# s>ss

# ----------------------------------------------------------------------
# overriding - inheritance should be present.using super can get parent class .so python supports overriding
# method overriding
# same number of parameters,same name, 2 class
# Method overriding occurs when a subclass (like Son) defines a method with the same name as a method in its superclass (like Father).
# Here, the phone() method in the Son class overrides the phone() method from the Father class.
# When you call s.phone(), Python first looks for the phone() method in the Son class and executes it. This is method overriding.
# class Father:
#     def phone(self):
#         print("Father class")

# class Son(Father):
#     def phone(self):
#         print("Son class")
#         super().phone()
# s = Son()
# s.phone()


# constructor overriding
# class Father:
#     def __init__(self):
#         print("Father class")

# class Son(Father):
#     def __init__(self):
#         print("Son class")
#         super().__init__()
# s = Son()


# ----------------------------------------------------------------------------
# Encapsulation
# access specifiers - public ,private,protected
# public - attributes and function can be accessed ouside the class
# class Father:
#     name = "abc"
#     def __init__(self):
#         print("working")

#     def phone(self):
#         print("Father can only call")

# s=Father()
# s.phone()
# print(s.name)

# private - attributes nd function have __ in variable name
# attributes and function should be called from inside class
# class Father:
#     __name = "abc"
#     def __init__(self):
#         print("working")
#         print(self.__name)
#         self.__phone()

#     def phone(self):
#         print("Father can only call")

# s=Father()
# s.__phone() #'Father' object has no attribute '_Father__phone'. Did you mean: '_Father__name'?

# protected -  attributes nd function have __ in variable name
# can be accessed from its class and subclass
# class Father:
#     _name="abc"
#     def __init__(self):
#         print("working")

#     def phone(self):
#         print("Father can only call")

# class Son(Father):
#     def __init__(self):
#         print("son")
#         print(self._name)
#         self._phone()

# s=Father()
# print(s._name)

# -----------------------------------------------
# some methods
# class A:
#     def show1(self):
#         print("a")

# class B(A):
#     def show2(self):
#         print("b")

# class C:
#     def show3(self):
#         print("c")

# class D(C):
#     def show4(self):
#         print("d")

# b1=B()
# d1=D()
# print(issubclass(B,A))
# print(issubclass(C,A))
# print(isinstance(b1,B))#b1 is instance of A and B
# print(isinstance(d1,B))#
# print(isinstance(d1,C))#d1 is instance of D and C(since C is parent clss)

# --------------------------------------------------------
#attribute methods - hasattr,getattr,setattr,delattr
# class Student:
#     name="ammu"
#     age=10
#     course="python"

# s=Student()
# print(s.name)
# print(hasattr(s,"name"))#cheks whether attribute present or not
# print(hasattr(s,"mark"))

# print(getattr(s,"name"))
# print(getattr(s,"mark"))#AttributeError: 'Student' object has no attribute 'mark'

# setattr(s,"name","anu")
# print(s.name)#print after setting name
# setattr(s,"mark",100)
# print(s.mark)#mark attribute not present therefore it create new attribute mark with given value

# delattr(s,"age")#AttributeError: 'Student' object has no attribute 'age'. since s is given so give student
# print(s.age)
# delattr(Student,"age")
# print(s.age)

#Create a class Student with class variables School
# a. Create a parameterised constrctor with id ,name and age
# b. Create instance of the class with id=1 ,name=Sara, age=10 and id =2,name ="Jose", age=20
# c. Access value of attributes of an instance using built in function
# d. Change the name attribute from Jose to Kris of defined instance 
# e. Check if class Student has place attribute.If class Student has no place ttribute then 
#   create it using the built-in method 

# class Student:
#     school="quest"
#     def __init__(self,id,name,age):
#         self.id=id
#         self.name=name
#         self.age=age
#         # print(self.id)
#         # print(self.name)
#         # print(self.age)

# # s1=Student(1,"Sara",10)
# s2=Student(2,"Jose",20)

# # print(getattr(s1,"id"))
# # print(getattr(s1,"name"))
# # print(getattr(s1,"age"))
# # print(getattr(s2,"id"))
# # print(getattr(s2,"name"))
# # print(getattr(s2,"age"))

# setattr(s2,"name","Kris")
# print(getattr(s2,"name"))
# print(s2.name)

# if hasattr(s2,"place"):
#     print(getattr(s2,"place"))
# else:
#     setattr(s2,"place","ekm")
#     print(getattr(s2,"place"))

#-----------------------------------------------------------------

# # docstring - triple quots inside class wont be printed in terminal
# # to print that, docstring is used
# class A:
#     """This is a class of A"""
#     def show(self):
#         print("hello")
# class B(A):
#     """this is a class of B"""
#     def display(self):
#         print("hai")
# class C(A):
#     def study(self):
#         print("study")
# b=B()
# c=C()
# print(A.__doc__)
# print(B.__doc__)

# """hello hai""" #as comment

# print("""hello
#        hai           hello
#        hai           hello""") #printing multiple lines


#-------------------------------------------------------
# instance method example-have a parameter self ,
# no decorators,can access both class and object
# modify both object's and class's state
class Student:
    class_variable=0 # Class variable shared by all instances
    def __init__(self,name):
        self.name=name # Instance variable unique to each instance
    def modify(self,newname):
        self.name=newname 
        self.__class__.class_variable+=1 #class variable changes for all objects 
# __class__ is a special attribute that allows an
# instance of class to access its class
s=Student("ammu")
print(s.name)
print(Student.class_variable)
s.modify("anu")
print(s.name)
print(Student.class_variable)
print(Student.class_variable,"pppppppppppp")


# class method example -can't modify using object but can modify using class 
# class method example
class Student:
    class_variable=0
    def __init__(self,name):
        self.name=name
    @classmethod
    def modify(cls):
        # self.name=newname
        # self.__class__.class_variable+=1
        cls.class_variable+=1 #can modify only class state

s=Student("ammu")
print(s.name)
print(Student.class_variable)
# s.modify("anu")#obj vech modify chyn pattilla pkshe cls vech modify chyn pattm
Student.modify()
print(Student.class_variable,"ppppppp")



# # static method example
# can't access using self and cls
class Student:
    class_variable=0
    def __init__(self,name):
        self.name=name
    @staticmethod
    def modify(a,b):
        # self.name=newname
        # self.__class__.class_variable+=1
        # cls.class_variable+=1
        print(a+b)

s=Student("ammu")
# print(s.name)#cant modify obj
# print(Student.class_variable)
Student.modify(10,20)
# print(Student.class_variable,"ppppppp") cant modify class variable

#--------------------------------------------
# destructor - after the object inte ref dlte chymbo 
class Student:
    def __init__(self):
        print("constructor")
    def __del__(self):
        print("destructor","first")
    def hello(self):
        print("working")
s=Student()
# del s #ith vilichlm illelm destructor invoke aavm

# s1=Student()
# s2=Student()
# s1.hello()
# del s
# del s1
# __del__() method is known as destructor
# it is called when all references to the object have been deleted
# that is when an object is garbage collected
# garbage collector that handles memory management automatically


# -------------------------------------------
# abstraction
# from abc module import ABC class and abstract method
from abc import ABC,abstractmethod
class Polygon(ABC):
    @abstractmethod
    def area(self):
        pass
class Rectangle(Polygon):
    def area(self):
        print("area")

r = Rectangle()
r.area()



# Abstract Base Class (ABC):
# An abstract base class is a class that cannot be instantiated directly. 
# It serves as a blueprint for other classes.
# In Python, you can create an abstract base class by inheriting from ABC (from the abc module).
# Abstract Method:
# An abstract method is a method that is declared but contains no implementation (just a placeholder). 
# It's meant to be implemented by subclasses.
# In Python, you declare an abstract method using the @abstractmethod decorator.
# Any subclass of the abstract class must override and implement the abstract method. 
# If it doesn't, the subclass also becomes abstract and cannot be instantiated.

# What Happens:
# Polygon (Abstract Base Class):
# Polygon is an abstract base class, and it has an abstract method area(). 
# This means that Polygon cannot be instantiated directly.
# The @abstractmethod decorator ensures that any class inheriting from Polygon must implement the area() method.
# Rectangle (Concrete Class):
# Rectangle is a subclass of Polygon. 
# It must implement the abstract method area() from the Polygon class.
# Rectangle provides an implementation for the area() method (here, it just prints "area").
# Instantiation:
# You create an instance of the Rectangle class using r = Rectangle(). 
# This is valid because Rectangle has implemented the abstract area() method.
# When you call r.area(), it prints "area" as expected.

# Why Abstract Base Classes Are Useful:
# They ensure that certain methods must be implemented by subclasses, enforcing a consistent interface across different classes.
# In your case, any class inheriting from Polygon (like Rectangle) must implement the area() method, ensuring that every Polygon-derived class will have an area() method.
# If you didn't implement the area() method in Rectangle, Python would raise a TypeError, as abstract methods must be implemented in concrete subclasses.