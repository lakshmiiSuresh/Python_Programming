# code having error is written try block
# try kodkkuvanel enthaylm except venam
try:
    a=int(input("enter a first number: "))
    b=int(input("Enter a second number: "))
    print(a/b)
except:# exceptions ine handle cheyum(general)
    print("zero division error")
else:#try il error illengil else print aavm
    print("no error")
finally:
    print("always excecutes")
print("stop")#ith work aavilla..error indel

# except il oro error kodth cheya
try:
    a=int(input("enter a first number: "))
    b=int(input("Enter a second number: "))
    print(a/b)
except ZeroDivisionError:
    print("zero division error first")


try:
    a=[1,2,3]
    print(a[3]) #IndexError: list index out of range
except IndexError:
    print("index error first")


try:
    a=int(input("enter a first number: "))#enter il alphabet kodkkmbo exception varum
    print(a)
except ValueError:
    print("Value error first")


try:
    print(a)
except NameError:
    print("name error first")


try:
    dict1={"name":"laks"}
    print(dict1["age"])
except KeyError:
    print("key error")

try:
    from math import cube #cube illa math modil
except ImportError:
    print("import error")

try:
    print("10"+10) #string um num um + chyn pttillh
except TypeError:
    print("type error")


try:
    age=int(input("enter your age: "))
    if age<18:
        raise #calls exception
    else:
        print("eligible for voting")
except:
    print("not eligible for voting")


try:
    age=int(input("enter your age: "))
    if age<18:
        raise TypeError #ivide age il typeonnm illah bust still aa error ilekk pokm
    else:
        print("eligible for voting")
except TypeError:
    print("not eligible for voting")


try:
    age=int(input("enter your age: "))
    if age<18:
        raise ValueErrorError
    else:
        print("eligible for voting")
except ValueError:
    print("not eligible for voting")



class Ageerror(Exception):#inheriting form exception class
    pass
try:
    age=int(input("enter your age: "))
    if age<18:
        raise Ageerror
    else:
        print("eligible for voting")
except Ageerror:
    print("not eligible for voting")


try:
    a=10
    b=5
    assert a>b,"a is less than b"
    print("a is greater than b")#since assert is true prints nxt line of code
except AssertionError as msg:
    print(msg)


try:
    a=10
    b=300
    assert a>b,"a is less than b"#since condtn false exception msg prints
    print("a is greater than b")
except AssertionError as msg:
    print(msg)

