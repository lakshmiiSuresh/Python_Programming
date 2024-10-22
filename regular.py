# import re module
import re

# s = "this is something special"
# x = re.findall("i",s) #to find all 'i' in s
# print(x)

# s = "this is something special"
# x = re.findall("y",s) # if not present it will return empty list
# print(x)

# s = "this is something special"
# x = re.findall("is",s) 
# print(x)

# special sequences -\
# s = "this is something special"
# x = re.findall("\s",s) # to get spaces in s
# print(x)

# s = "this is something special1222"
# x = re.findall("\S",s) # opposite of \s i.e all characters except spaces in s
# print(x)

# s = "this is 1222something@$$### special133333"
# x = re.findall("\d",s) #to get numberss
# print(x)

# s = "this is something special$$$$$1222"
# x = re.findall("\D",s) # all characters including spaces but except numbers.opposite of \d
# print(x)

# s = "this is something$$$$^^^ special122333"
# x = re.findall("\w",s) #no special charaters and space i.e alphabets and numbers
# print(x)

# s = "this is something$$$ special"
# x = re.findall("\W",s) # special characters and spaces
# print(x)

# s = "this is something$$$$^^^ special122333"
# x = re.findall("\Athis",s)  #checks whether s starts with 'this' .if yes it will print that
# print(x)

# s = "this is something$$$$^^^ special122333"
# x = re.findall("\Ais",s) #starting not with 'is' so it will return empty set
# print(x)

# s = "this is something$$$$^^^ special122333"
# x = re.findall("special122333\Z",s) #checks if s ends with special122333
# print(x)

# s = "this is something$$$$^^^ special122333"
# x = re.findall(r"\bthis",s) #\b to check if any of words  starts with this.if present it will print that in list
# print(x)

# s = "this is something$$$$^^^ special122333"
# x = re.findall(r"\bsome",s) #starting of word something
# print(x)

# s = "this is something$$$$^^^ special122333"
# x = re.findall(r"122333\b",s) #checks if sentence ends with 122333
# print(x)

# s = "this is something$$$$^^^ special122333"
# x = re.findall(r"$$^^^\b",s) #checks if the sentence ends with 
# print(x)

# s = "this is something$$$$^^^ special122333"
# x = re.findall(r"\Bthin",s) #nor starting nor ending .thin is present in something
# print(x)

# s = "this is something$$$$^^^ special122333ng ng"
# x = re.findall(r"\Bng$",s) 
# print(x)

# s = "this is something$$$$^^^ special122333"
# x = re.findall(r"\Bcial1",s) 
# print(x)



# =============================================================
# set -[]
# s = "this is something@@$## special12345"
# x = re.findall("[agspr]",s) #returns list with the characters present in set is present in s
# print(x)

# s = "AGSHHDKLLNCNNZXXthis is something@@$## special12345"
# x = re.findall("[a-z]",s) #returns only small letters from a to z
# print(x)

# s = "AGSHHDKLLNCNNZXXthis is something@@$## special12345"
# x = re.findall("[A-Z]",s) #returns only capital  letters from A-Z
# print(x)

# s = "AGSHHDKLLNCNNZXXthis is something@@$## special12345"
# x = re.findall("[0-9]",s) #returns numbers present in s
# print(x)

# s = "AGSHHDKLLNCNNZXXthis is something@@$## special12345"
# x = re.findall("[^a-z]",s) #all other than small letters
# print(x)

# s = "AGSHHDKLLNCNNZXXthis is something@@$## special12345"
# x = re.findall("[^A-Z]",s) #all other than capital letters
# print(x)

# s = "AGSHHDKLLNCNNZXXthis is something@@$## special12345"
# x = re.findall("[^0-9]",s) #all other than capital letters
# print(x)

# s = "AGSHHDKLLNCNNZXXthis is something@@$## special12345"
# x = re.findall("[^ASD]",s) #checks starting with ASD and print all except
# print(x)

# s = "AGSHHDKLLNCNNZXXthis is something@@$## special12345"
# x = re.findall("[12345$]",s) #checks ends with 12345
# print(x)

# .,,$ - metacharacters
# s = "hello AGSHHDKLLNCNNZXXthis is helo something@@$## heoo special12345"
# x = re.findall("he.o",s) #one character in place of he.o
# print(x)

# s = "hello AGSHHDKLLNCNNZXXthis is something@@$## special12345"
# x = re.findall("he.o",s)
# print(x)

# s = "heo AGSHHDKLLNCNNZXXthis is something@@$## special12345" #one character should be present. wont consider heo
# x = re.findall("he.o",s) 
# print(x)

# import re
# s = "hello AGSHHDKLLNCNNZXXthis is helo something@@$## special12345"
# x = re.findall("he.+o",s)
# print(x)

# s = "helo AGSHHDKLLNCNNZXXthis is hel smething@@$## special12345" #one character
# x = re.findall("he.+o",s)
# print(x)

# import re
# s = "heo AGSHHDKLLNCNNZXXthis is hel smething@@$## special12345" #zero character not possible
# x = re.findall("he.+o",s)
# print(x)

# s = "helo AGSHHDKLLNCNNZXXthis is hel smething@@$## special12345" 
# x = re.findall("he.*o",s)
# print(x)

# s = "heo AGSHHDKLLNCNNZXXthis is hel smething@@$## special12345" 
# x = re.findall("he.*o",s)
# print(x)

# s = "helo AGSHHDKLLNCNNZXXthis is hel smething@@$## special12345" 
# x = re.findall("he.?o",s)
# print(x)

# s = "heo AGSHHDKLLNCNNZXXthis is hel smething@@$## special12345" 
# x = re.findall("he.?o",s)
# print(x)

# s = "hello AGSHHDKLLNCNNZXXthis is hel smething@@$## special12345" 
# x = re.findall("he.?o",s)
# print(x)


# s = "heo AGSHHDKLLNCNNZXXthis is hel hell hello smething@@$## special12345" 
# x = re.findall("hel|hell",s) #adyathe ondonn nokkm undegil ath
# print(x)

# s = "heo AGSHHDKLLNCNNZXXthis is hel hell hello smething@@$## special12345" 
# x = re.findall("hello|hell",s) #adyathe ondonn nokkm undegil ath
# print(x)

# import re
# s = "heo AGSHHDKLLNCNNZXXthis is hel hell hello smething@@$## special12345" 
# x = re.findall("he.{2}o",s) 
# print(x)

# import re
# s = "heo AGSHHDKLLNCNNZXXthis is hel hell hello smething@@$## special12345" 
# x = re.findall("[a-z]+",s) #only small letter groups
# print(x)

# s = "heo AGSHHDKLLNCNNZXXthis is hel hell hello smething@@$## special12345" 
# x = re.findall("[0-9]+",s) #set of number groups
# print(x)


# + - one or more occurence
# * - zero,one or more occurence
# ? - zero or one occurence only

# # ====================================================
# import re
# text = "Hello, my name is John.I have two cats, Mia and Max."
# x = re.findall(r"\b\w{3}\b",text)
# print(x)

# text = "Contact info@gmail.com or support@example.com."
# # y = re.findall(r"\b\w+@\w+\.\w+\b",text) #-special sequences
# y = re.findall(r"\b[a-zA-Z-0-9]+@[a-zA-Z0-9]+\.[a-zA-Z0-9]+\b",text) #-using []
# print(y)

# text = "Important dates: 2022-01-01, 2023-05-15, and 2023-12-31"
# # z = re.findall(r"\b[0-9]+-[0-9]+-[0-9]+\b",text)
# z = re.findall(r"\d{4}-\d{2}-\d{2}\b",text)
# print(z)

# import re
# text = "ammu hello my name is ammu"
# x = re.search("ammu",text)
# print(x)


# import re
# text = "hello my name is"
# x = re.search("ammu",text)
# print(x)

# import re
# text = "ammu hello my name is ammu how are you ammu"
# x = re.search("ammu",text)
# print(x)

# print(x.span())
# print(x.start())
# print(x.end())
# print(x.group())
# print(x.string)

# import re
# text = "hello AMMU how are you ammu"
# x = re.search("ammu",text)
# print(x)

# import re
# text = "hello AMMU how are you ammu"
# x = re.search("ammu",text,re.IGNORECASE)
# print(x)

# import re
# text = "hello AMMU how are you ammu"
# x = re.search("^hello",text)
# print(x)

# import re
# text = "hello AMMU how are you ammu"
# x = re.search("hello$",text)
# print(x)

# import re
# text = "hello AMMU123 how456 are you ammu"
# x = re.search("\d+",text)
# print(x)

# import re
# text = "hello AMMU how are you ammu"
# x = re.split(" ",text)
# print(x)

# import re
# text = "hello ammu123 how are456 you ammu789"
# x = re.split(" ",text,2)
# print(x)

# import re
# text = "hello ammu123 how are456 you ammu789"
# x = re.split(" ",text,2)
# print(x)

# import re
# text = "hello ammu123 how are456 you ammu789"
# x = re.split("\d+",text)
# print(x)

# import re
# text = "hello hello hello hello"
# x = re.split("ll",text)
# print(x)

# import re
# text = "apple123orange123grapes123mango123"
# x = re.split("\d+",text)
# print(x)

# import re
# text = "apple-orange:grapes|mango"
# x = re.split("[-:|]",text)
# print(x)

# import re
# text = "hello hello hello hello "
# x = re.sub("ll","@",text)
# print(x)

# import re
# text = "hello hello hello hello "
# x = re.sub("ll","@",text,2)
# print(x)

# import re
# text = "my name is ammu and my phone number is 9384943432"
# x = re.sub("\d{10}","XXXXXXXXXX",text,2)
# print(x)

# import re
# text = "hello hello hello HELLO HELLO"
# x = re.sub("ll","@",text)
# print(x)

# import re
# text = "hello hello hello HELLO HELLO"
# x = re.sub("ll","@",text,5,re.IGNORECASE)
# print(x)

# =====================
# match checks the starting of sentence if not starting with that gives none
import re
text = "hello my name is ammu"
x = re.match("ammu",text)
print(x)

# starts  with hello so it gives match
import re
text = "hello my name is ammu"
x = re.match("hello",text)
print(x)