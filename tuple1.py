#tuple is immutable

# x = (1,2,3,4,5,6)
# print(type(x))
# print(len(x))

# y=("python","java","php")
# print(y)

# z = ("hai",4,5,"hello",True)
# print(z)

s=("welcome","python")
print(type(s))

s=("hai")
print(type(s))#if written like this type will be string
s =(10)
print(type(s))#type will be int

# write a tuple with single variable 50
s=(50,)#since , is present its type will be tuple
print(type(s))

p=(True,False)
print(type(p))

z = z = ("hai",4,5,"hello",True)
print(z[0])
print(z[-1])
print(z[1:4])
print(z[-4:-1])
print(z[::-1])

z = z = ("hai",4,5,"hello",True)
print(dir(z))

z = ("hai",4,5,"hello",True,4,5)
print(z.index(4))
print(z.count(4))

#for loop
x = (1,2,"hai")
for i in x:
    print(i)

x = (1,2,"hai")
for i in range(len(x)):
    # print(i)
    print(x[i])

#while
x = (1,2,"hai")
i=0
while i<len(x):
    print(x[i])
    i+=1

# #list is mutable therefore apple is changed 
# in 0th index and can also delete within the same
# x = ["hai","hello"]
# x[0]="apple"
# print(x)
# del x[0]
# print(x)

#tuple is immutable so convert first to list
x = ("python","php","java","dotnet")
y = list(x)
print(y)
y[0]="apple"
print(y)
del y[2]
print(y)
z = tuple(y)
print(z)

# #1. reverse the tuple x =(10,20,30,40,50)
# x =(10,20,30,40,50)
# y=x[::-1]
# print(y)

# #2. access the value 20 from the tuple .tuple1 = ("orange",[10,20,30],[5,15,25]) 
# tuple1 = ("orange",[10,20,30],[5,15,25]) 
# y = tuple1[1][1]
# print(y)

#3. create a tuple with single item 50 - imp question
x = (50,)
print(type(x))
print(x)

#4. modify the tuple  t1 = (11,[22,33],44,55).make 22 to 222
t1 = (11,[22,33],44,55)
#or----
# x = t1[1][0]=222
# print(t1)
#------
l = list(t1)
l[1][0] = 222
# print(l)
t2 = tuple(l)
print(t2)


#5. check if all items in the tuple are the same t1 = (45,45,45,45)
t1 = (45,45,45,45)
for i in t1:
    if i!=45:
        break
        print("item other than 45 found")
    else:      
        print("All items in te tuple are same")
# or
t1 = (45,45,45,45)
n = t1[0]
for i in t1:
    if i==n:
        print("same")

# or 
t = (45,45,45,45)
print(t.count(t[0])==len(t))  


#6.Count the number of occurences of item 50 from a tuple t1 =(50,10,60,70,50)
t1 =(50,10,60,70,50)
# or-----------
# y = t1.count(50)
# print(y)
# -------------
count=0
for i in range(len(t1)):
    if t1[i]==50:
        count+=1
print("number of occurences of item 50 is:",count)


# operators in tuple
t1=(10,20,30,40,50)
t2=(100,200,300,400,500,10)
print(t1+t2)
x = t1+t2
print(x)
t1+=t2
print(t1)

print(t1*3)#multiplication

print(100 in t2)#membership

t1=(10,20,30,40,50)
del t1
print(t1)

courses = ("python","java","dotnet","php") #packing a tuple
(a,b,c,d) = courses #unpacking
print(a)
print(b)
print(c)
print(d)

courses = ("python","java","dotnet","php") 
(a,b,c) = courses 
print(a)
print(b)
print(c)


courses = ("python","java","dotnet","php") 
(*a,b,c) = courses
print(a)
print(b)
print(c)


courses = ("python","java","dotnet","php") 
(*a,*b,c) = courses
print(a)
print(b)
print(c)
