# print('Hello')
# print("Hello")

# print("That is Raju's house")

# a = "Hello"
# # print(a)
# a = "hai"
# print(a)
# del a
# print(a) #deleted a 

# a = "hai"
# s =a*5
# print(s)

# s= "laks" in "lakshmi"
# print(s)

# for x in "banana":
#     print(x)

# a = "Hello World"
# print(len(a))

# txt = "The best things in life are free"
# print("free" in txt)
# print("free" not in txt)

# a = "Hello world"
# print(a[1]) #indexing
# print(a[11]) #IndexError: string index out of range
# # slicing - sequence[start:end:step]
# # start: The index where the slice starts (inclusive).
# # end: The index where the slice ends (exclusive).
# # step: The interval between each element in the slice (optional).
# a = "Hello world"
# print(a[2:5])
# print(a[2:4])
# print(a[:5])
# print(a[:4])
# print(a[2:])
# print(a[-5:-2]) #starts from -5 and stops just before -2 i.e -3
# a = "Hello world"
# print(a[-5:-2:-1]) # empty string ,since from -5 to -2 direction is opposite of skip -1 
# a = "Hello world"
# print(a[-2:-5:-1])
# print(a[-2::-1] )
# a = "Hello world"
# print(a[::-2])

# a = "Hello"
# b = "Hai"
# c = a + b
# print(c)

# a = "Hello"
# b = "World"
# c = a+" "+b
# print(c)

#formating
# age = 26
# w = "hi"
# print("hello",w) #auto space will come
# print("hello"+w) #no space
# txt = f"My name is john , I am {age}"
# print(txt)
# # or
# print(f"I am lakshmi and i am {age} years old")

#----------------------------string methods---------------------
# s = 'hello World'
# print(s.capitalize())#first letter capital balance all small letter

# s = "Hello world"
# print(s.title()) #first letter of both the words capital
# s = "Hello wOrld"
# print(s.title())
# print(s.istitle())

# s= 'Hello world'
# print(s.upper())
# print(s.isupper())

# s = 'Hello World'
# print(s.lower())
# s= "hello"
# print(s.islower())

# s = 'Hello World'
# print(s.casefold())
# s = 'ß'
# print(s.lower())
# print(s.casefold())

# s = 'Hello world'
# print(s.count('o'))

# s = 'Hello world'
# print(s.find("o"))# index of first seen 'o'
# print(s.find("oro"))#if not present ,-1 will be printed

# s = "Hello world"
# print(s.index("o")) #index of first seen 'o'
# print(s.index("oro"))#display error since not present,ValueError: substring not found

# txt = "For only {price} dollors"
# print(txt.format(price  = 49))
# txt = "For only {price:.2f} dollors"
# print(txt.format(price = 24))

# s = "Hello World123"# since space is present. only alphabets and numeric should be present
# print(s.isalnum())
# s1 ="Helloworld123"
# print(s1.isalnum())
# s = "HelloWorld123!"
# print(s.isalnum())

# s = "Hello world" #space is present
# print(s.isalpha())
# s = "Hellohai"
# print(s.isalpha())

# s = '1234'
# print(s.isdecimal())
# s= '1234 '
# print(s.isdecimal()) #satisfy digits from 0 to 9

# s = '1001'
# s = "\u0030" #unicode for 0
# s = "\u00B2" #unicode for ²
# print(s.isdigit()) # satisfy digits from 0 to 9 and unicode


# s="Hello world"
# print(s.isspace())
# s=' '
# print(s.isspace())

# s = "Hello world"
# for i in s:
#     if i.isspace():
#         print('T')

# s = 'Hello world'
# print('-'.join(s))
# s = 'Hello world'
# print(' '.join(s))

# s = 'Hello world!'
# print(s.replace('Hello','Hi'))

# s = "Hello World"
# print(s.split())# space ulledth vach split cheym sentence ine,output will be in list

# s = "Hel1lo Wor1ld1"
# print(s.split('1'))

# s = "Hello\nworld\n"
# print(s.splitlines())
# s = "Hello\nworld\n"
# print(s.splitlines())
# s = "Hello\nworld\t"
# print(s.splitlines())

# s = "Hello World!"
# print(s.swapcase())

#----------------------------------------------

# s = "banana"
# x = s.center(20)
# print(x)

# s = "banana"
# x = s.center(20,'0')#make alignment in the center
# print(x)

# s = "My name is ß" #encode another language letters
# print(s.encode())

# s = "Hello, welcome to my world."
# print(s.endswith("."))

# s = "H\te\tl\tl\to"
# print(s)
# print(s.expandtabs())
# print(s.expandtabs(1))
# print(s.expandtabs(2))
# print(s.expandtabs(3))
# print(s.expandtabs(4))
# print(s.expandtabs(5))
# print(s.expandtabs(6))
# print(s.expandtabs(7))
# print(s.expandtabs(8))
# print(s.expandtabs(9))
# print(s.expandtabs(10))

# mk = {'x':'Alice','y':89,'z':'Maths'}
# text = '{x} scored {y} marks in {z}'
# print(text.format_map(mk))

# print('{x} scored {y} marks in {z}'.format_map( {'x':'Alice','y':89,'z':'Maths'}))


# x = "Company123"
# print(x.isascii())#alphabets, numbers are all having ascii values so isascii() will give true . if any other anguage alphabets are given it wil give false

# x ="C"
# print(x.isascii())

# x = "c"
# print(x.isascii())

# x = "5"
# print(x.isascii())

# x = "ß"
# print(x.isascii())# other language so issascii gives false


# b = "_Demo"
# print(b.isidentifier())
# b = "1_Demo"
# print(b.isidentifier())


# txt = "Hello Sam!"
# mytable = str.maketrans("S","P")
# print(mytable)
# print(txt.translate(mytable))

# txt = "I could bananas eat bananas all day"
# print(txt.partition("bananas"))

# txt  = "I could eat bananas all day, bananas are my favourite fruit"
# print(txt.rpartition("bananas"))

# s = "malayalam"
# print(s.rfind('la'))#finding from right but indexing from front
# s = "malayalam"
# print(s.rfind('my'))

# s = 'malayalam'
# print(s.rindex('la')) 
# s = 'malayalam'
# print(s.rindex('my'))#ValueError: substring not found

# x = "banana"
# print(x.ljust(20,"0"))

# x = "banana"
# print(x.rjust(20,"0"))

# a = "C,Python,Java,C++"
# print(a.rsplit(","))

# a = "C,Python,Java,C++"
# print(a.rsplit(",",2))

# txt = "Hello,welcome to my world."
# x = txt.startswith("Hello")
# print(x)


# txt = "     banana      "
# x = txt.strip()
# print("of all fruits",x,"is my favorite")


# txt = "     banana      "
# x = txt.rstrip()
# print("of all fruits",x,"is my favorite")


# txt = "     banana      "
# x = txt.lstrip()
# print("of all fruits",x,"is my favorite")

# Removing specific characters
# text = "###Hello, World!###"
# stripped_text = text.strip("#")
# print(stripped_text) 

# mydict = {83: 80}
# txt = "Hello Sam!"
# print(txt.translate(mydict))

# a="50"
# print(a.zfill(10))


# a = input("Enter a string: ")
# length = len(a)
# lcount = 0
# ucount = 0
# scount = 0
# for i in range(length):
#     if a[i].islower():
#         # print(a[i].upper(),end= " ")
#         lcount+=1
#     elif a[i].isupper():
#         # print(a[i].lower(),end=" ")
#         ucount+=1
#     else:
#         scount+=1
# print("lower case count is",lcount)
# print("upper case count is",ucount)
# print("space count is",scount)


# s=list("parvathy")
# print(dir(s))