# open(filename,mode)

f = open("abc.txt") #default in read mode
print(f.read())
f.close()

f = open("abc.txt","r") 
print(f.read())
f.close()

f = open("abc.txt","r") 
# print(f.read(7))#specify how many characters you want to return
# print(f.read(8))
print(f.read(9))#for example: in abc.txt there are two lines hellohai and welcome. hellohai will printed in f.read(8) since 8 letters
print(f.read(10))#but welcome line's 'w' wont get printed with f.read(9). for that you need to use f.read(10)
f.close()

f = open("abc.txt","r") 
print(f.readline())
print(f.readline())
f.close()

f = open("abc.txt","r") 
print(f.readlines()) #output as list
f.close()

f = open("abcd.txt","r") #error : No such file or directory: 'abcd.txt'
print(f.read())
f.close()

#------------------------
f = open("abc.txt","w") #if contents in abc.txt it will overwrite
f.write("hello")
f.close()

f = open("abcd.txt","w") #since no txt file named abcd ,it will create new and write hello to it
f.write("hello")
f.close()
#--------------------------

f = open("abc.txt","a") #since abc.txt already exists hai will get appended to hello in abc.txt
f.write("hai")
f.close()

f = open("abd.txt","a") #since abd.txt is absent , it will create new text file named abd.txt and append to it
f.write("hai")
f.close()
#---------------------------

# f=open("abc.txt","x") #error: File exists: 'abc.txt'
# f.close()

# f=open("ab.txt","x")
# f.close()

#----------------------------

#using different variables f andf1
f=open("numbers.txt","w")
f.write("10\n")
f.write("20\n")
f.write("15\n")
f.close()
f1=open("numbers.txt","r")
p = f1.readlines()
print(p)
g = [int(i) for i in p]
print(g)
u = max(g)
print(u)
f1.close()

#single variable
# f = open("numbers.txt","w")
# f.write("50\n20\n30")
# f = open("numbers.txt","r")
# p = f.readlines()
# m = [int(i) for i in p]
# g = max(m)
# print(g)
# f.close()


# create a file with some text then count and print the number of words in the file
# f=open("words.txt","x")
# f.write("Hai\nhello\nwelcome")
f = open("words.txt")
p= f.read()
print(p)
l=p.split()
print(l)
print(len(l))
f.close()


#seek 
f = open("abc.txt","r")
a = f.seek(5)#gives position from 0 to 5 and start from 5th position i.e Moves the file pointer to the 5th byte in the file
print(a)
x = f.read(5)#reads 5 characters
print(x)
f.close()

#tell
f = open("abc.txt","r")
a=f.tell() # Returns the current position of the file pointer, which is at the beginning
print(a)
x = f.read(5)
print(x)
a=f.tell() #Returns the current position of the file pointer after reading
print(a)
f.close()

#read file from another folder
f = open(r"C:\Users\SURESH\OneDrive\Documents\sample\sample1.txt.txt","r") #r is rowstring used to consider slash as slash and n as n not new line
print(f.read())
f.close()

f = open(r"C:\Users\SURESH\OneDrive\Documents\sample\sample1.txt.txt","a") 
print(f.write("10\n"))
f.close()


import os
import shutil
# os.remove("abcde.txt") #to remove a file import os module and use remove
# os.rmdir("hello")# to delete empty folder
# shutil.rmtree("hello") #to remove folder with files,import shutil and use rmtree


with open("abc.txt","r") as file: #with statement can be used to open file
    x = file.write("worked")
    print(x)
file.close()


input1 = [2,7,11,15]
target = 9 
# input1 = [1,4,2,3,7]
# target = 6
output = [0,1]

# input1 = [1,4,3,6,7]
# target = 7
# for i in range(len(input1)):
#     for j in range(len(input1)):
#         s = input1[j] + input1[j+1]
#         if s == target:
#             break
# print(j)
# print(j+1)
    
        

    
   
        
    

   

    
    


