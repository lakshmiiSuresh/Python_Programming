# x = [10,20,30,40,50]
# print(x)

# print(len(x))

# a=list()
# print(a)

# a=list
# print(a)

# x = ["python","java","C"]
# print(x)

# x=[True,False]
# print(x)

# x = [10,20,30,40,50,"python","java","C",True,False]
# # print(x)

# # print(type(x))

# x = ["laks","par","vaish"]
# for i in x:
#     print(i)

# for i in range (len(x)):
#     print(x[i])

# x = [10,20,30,40,50,"python","java","C",True,False]
# print(x[0])
# print(x[-1])
# print(x[2:6])
# print(x[-6:-2])
# print(x[::-1])

# a = "hai"
# x = list(a)
# print(x)

# a = "hai"
# l1=[]
# l1.append(a)
# print(l1)

# x = ["laks","par","vaish"]
# print(dir(x))

# x = ["python","java","C"]
# x.append("dotnet") # element will be added at the last of list
# print(x)

# x = ["python","java","C"]
# x.insert(2,"datascience") # fist of all we need to specify which position to be inserted then element to be inserted
# print(x)

# x = ["python","java","C"]
# z = [10,20,30,40,50]
# # x.append(z) #z list full aaitttu append aavm x ilottu
# x.extend(z) # z list ile oro elements append aavm x ileek
# print(x)

# x = ["python","java","C"]
# z = "haaai"
# x.append(z) #z list full aaitttu append aavm x ilottu
# x.extend(z) # z list ile oro elements append aavm x ileek
# print(x)

# x = ["python","java","C"]
# p = "hello"
# x.extend(p)
# print(x)

#--------------------------------------------------------------------
#wrong
# n = int(input("Enter a number: "))
# e = ['one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
# for i in range(1,20):
#     if n==i:
#         if n%i == 0:
#             print(e[i-1])
# for i in range(20,30):
#     if n==20:
#         print('twenty')
#     elif n==i and n!=20:
#        if n%i == 0:
#         print('twenty'+ '-' + e[i-1])

#----------------------------------------------------------------------------------

# n = int(input("Enter a number: "))
# e = ['zero','one','two','three','four','five','six','seven','eight','nine']
# en = ['ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
# f =['','','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
# em = ''
# if 0<=n<=9:
#     em = em+ e[n]
#     print(em)
# elif 10<=n<=19:
#     em = em+ en[n-10]
#     print(em)
# elif 20<=n<100:
#     em = em + f[n//10] +' '+ e[n%10]
#     print(em)
# else:
#     print("Hundred")


# print("Enter 10 numbers: ")
# list1=[]
# for i in range(10):
#     list1.append(input())
# or
#     numbers = int(input("enter the number"))
#     list1.append(numbers)
# print(list1)


# x =["M","na","i","ke"]
# y =["y","me","s","lly"]
# xy = []
# if len(x)==len(y):
#         for i in range(len(x)):
#                 xy.append(x[i] + y[i])
# print(xy)

# list1 = ["hello","hai"]
# list2 = ["dear","madam"]
# list3 = []
# for i in range(len(list1)):
#         for j in range(len(list2)):
#                 list3.append(list1[i] +" "+ list2[j])
# print(list3)

# -------------------------------List methods---------------------------------------

# z = ['My', 'name', 'is', 'kelly',"name"]
# # print(dir(z))

# print(z.index("name"))#will get the index position.if element is repeated ,index position of first occured element will be fetched

# z = ['My', 'name', 'is', 'kelly',"name"]
# print(z.count("name"))

# z.clear()
# print(z)


# z = ['My', 'name', 'is', 'kelly',"name"]
# z.reverse()
# print(z)


# z = ['My', 'name', 'is', 'kelly',"name"]
# z.sort()#ascending.to get desc reverse it.Priority for capital letters after A only a occurs or after Z only a occurs
# print(z)

# z = ['My', 'name', 'is', 'kelly',"name"]
# z.pop()#delete element from last position of list
# print(z)

# z = ['My', 'name', 'is', 'kelly',"name"]
# x = z.pop(2)#deleted from 2nd index
# print(z)
# print(x) # to know which element is popped assign the popped element to a variable and print it

# z = ['My', 'name', 'is', 'kelly',"name"]
# # z.remove("My")
# z.remove("name") #first name will be removed.only the first occurence will be removed
# print(z)

# x = z.copy()
# print(x)

#----------------------different ways of iterating list---------------------------
# x = [1,2,3,"hai"]
# for i in x:
#         print(i)


# x = [1,2,3,"hai"]
# for i in range(len(x)):
#         print(x[i])


# x = [1,2,3,"hai"]
# i=0
# while i<len(x):
#         print(x[i])
#         i+=1
# ----------------------------------------------------------------------------------------


# WAP to add item 7000 after 6000 in the following list
# list2 =[10,20,[300,400,[5000,6000],500],30,40]
# list2[2][2].append(7000)    
# print(list2)   


# WAP  to extend it by adding the sublist["h","i","j"]
# in such a way that it look like the following list
# list5 = ["a","b",["c",["d","e",["f","g"],"k"],"l"],"m","n"]
# list6 = ["h","i","j"]
# list5[2][1][2].extend(list6)
# # list5[2][1][2].append("h")
# print(list5)


#WAP to remove all occurences of item 20
#-------------------------------------------
#wrong
# list4 = [5,20,15,20,25,50,20]
# for i in range(len(list4)):#length changes so cant use len in for loop
#         if list4[i] == 20:
#                 list4.remove(list4[i])
# print(list4)
#------------------------------------------

# list4 = [5,20,15,20,25,50,20]
# for i in list4:
#         if i == 20:
#                 list4.remove(i)
# print(list4)


# WAP to find value 20 in the list, and if it is present,replace it with 200. only update the first occurence of an item 
# list3 =[5,10,15,20,25,50,20]
# list4 = []
# for i in list3:
#         if i==20:
#                temp = i
#                i = 200 
#                list4.append(i)      
#                continue
#         else:
#                list4.append(i)
# print(list4) 

## or
# list3 =[5,10,15,20,25,50,20]
# list3.remove(20)
# list3.insert(3,200)
# print(list3)

# #or
# list3 =[5,10,15,20,25,50,20]
# s = list3.index(20)
# print(s)
# list3[s]=200
# print(list3)

# a = "have a nice day"
# new = a.split()
# print(new)
# print(new.reverse())
# print(" ".join(new))

# a = "have a nice day"
# x = a.split()
# y = x[::-1]
# z = " ".join(y)
# print(z)

#2. without duplicates
# l = [1,2,3,5,4,2,1,3,5,4]
# l1 = []
# for i in l:
#         if i not in l1:
#                 l1.append(i)
# print(l1)
# l1.sort()
# print(l1)

# # or
# l = [1,2,3,5,4,2,1,3,5,4]
# l1 =set(l)
# print(list(l1))

#3. sum of list items
# l = [1,2,3,5,4,2,1,3,5,4]
# sum = 0
# for i in range(len(l)):
#         sum = sum + l[i]
# print(sum)

#another method
# l = [1,2,3,5,4,2,1,3,5,4]
# z=sum(l)
# print(z)


# #4 find the maximum and minimum item in a list
# l1 = [11,84,56,19,73,56]
# l1.sort()
# #print(l1.sort()) it won't work
# print(l1)
# print("Minimum : ",l1[0])
# print("Maximum : ",l1[-1])
#or
# l1 = [11,84,56,19,73,56]
# minimum_value=min(l1)
# maximum_value=max(l1)
# print(minimum_value )
# print(maximum_value)
#

# l1 = [11,84,56,19,73,56]
# for i in range(len(l1)):
#         if l1[i]>l1[i+1]:
#                 temp = l1[i]
#                 l1[i]=l1[i+1]
#                 l1[i+1]=temp
# print(l1)



#----------------------list comprehension---------------------------

# x =[expression for i in itreable if condition]
# answer will be list
# #for
# a = "python"
# x = [i for i in a]
# print(x)

# # for with range
# x = [i*i for i in range(1,11)]
# print(x)

# # for with if condition
# s = [1,2,3,4,5,6,7,8,9,10]
# x = [i for i in s if i%2==0]
# print(x)

# #for with 2 ifs and if using and is same
# s = [1,2,3,4,5,6,7,8,9,10]
# x = [i for i in s if i%2==0 if i%5==0]
# x = [i for i in s if i%2==0 and i%5==0]
# print(x)

# #using if else
# s = [1,2,3,4,5,6,7,8,9,10]
# x = [i+1 if i>2 else i for i in s]#if if condition is true then i+1 works, if else is true then i will work
# print(x)


##1.l = ["madam","level","random","python","mom"]#print only palindrom words from list
# l = ["madam","level","random","python","mom"]
# x = [i for i in l if i==i[::-1]]
# print(x)

##2. p = ["hai" ,"hello","welcome"]#convert this string items to uppercase
# p = ["hai" ,"hello","welcome"]
# x = [i.upper() for i in p ]
# print(x)

# #3.x = [1,2,3,4,5]
# #  y =[2,3,5,6,8] #find common elements in the list
# x =[1,2,3,4,5]
# y =[2,3,5,6,8] 
# z = [i for i in x  if i in x and i in y]
# print(z)

#4.f = [-2,-1,5,1,2]#convert +ve numbers to true and -ve numbers to false
# f = [-2,-1,5,1,2]
# j = [True if i>0 else False for i in f ]
# print(j)

# #5. s = "list comprehension is simple" #remove all vowels
# s = "list comprehension is simple"
# # x =[" " if i in "aeiouAEIOU" else i for i in s ]
# x = [i for i in s if i not in "aeiouAEIOU"]
# print(" ".join(x))


# l = [10,20,30,40,50] #find half of all numbers
# x = [i//2 for i in l]
# print(x)

#--------------------------------matrix--------------------------------
# a = [[1,2],[3,4]]
# # print(a)
# for i in a:
#         # print(i)
#         for j in i:
#                 print(j,end=" ")
#         print()


# b = [[1,2,3],[4,5,6],[7,8,9]]
# for i in b:
#         for j in i:
#                 print(j,end=" ")
#         print()


## adding two matrices
# a =[[1,2],[3,4]]
# b =[[1,2],[3,4]]
# c =[[0,0],[0,0]]
# for i in range(len(a)):
#         for j in range(len(b)):
#                 c[i][j]=a[i][j]+b[i][j]
# print(c)
# for i in c:
#         for j in i:
#                 print(j,end=" ")
#         print()



# #creating a matrix
# rows = int(input("Enter the number of rows: "))
# cols = int(input("Enter the number of columns: "))
# main=[]
# for i in range(rows):
#         sub=[]
#         for j in range(cols):
#                 values=int(input("Enter the number: "))
#                 sub.append(values) #[1,2] [3,4]
#         main.append(sub) # [[1,2],[3,4]]
# print(main)
# for i in main:
#         for j in i:
#                 print(j,end=" ")
#         print()
                

# #3x3 multipliction
# a = [[1,2,3],[4,5,6],[7,8,9]]
# b = [[1,2,3],[4,5,6],[7,8,9]]
# c = [[0,0,0],[0,0,0],[0,0,0]]
# for i in range(len(a)): #i=0
#         for j in range(len(b)): #j=0                         #j=1                     #j=2
#                 k=0
#                 for k in range(len(c)): #k=0 k=1 k=2         #k=0 k=1 k=2             #k=0 k=1 k=2 
#                         c[i][j]=c[i][j]+ a[i][k]*b[k][j]
# print(c)


# # transpose of a matrix
# print("Original matrix: ")
# a = [[1,2],[4,5]]
# for i in a:
#         for j in i:
#                 print(j,end=" ")
#         print()
# print("Transpose matrix: ")
# for i in range(len(a)):
#         for j in range(len(a)):
#                 if i==j:
#                         print(a[i][j],end=" ")
#                 else:
#                         print(a[j][i],end=" ")                  
#         print()   

print("Original matrix: ")
a = [[1,2,3],[4,5,6],[5,7,8]]
for i in a:
        for j in i:
                print(j,end=" ")
        print()
print("Transpose matrix: ")
b = [[0,0,0],[0,0,0]]
for i in range(len(a[0])):
        for j in range(len(a)):
                if i==j:
                        print(a[i][j],end=" ")
                else:
                        print(a[j][i],end=" ")                  
        print()   
        





















    
   