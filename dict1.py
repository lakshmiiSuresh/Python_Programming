# x = {"name":"ammu","age":10,"place":"kochi"}
# print(x)
# print(len(x))
# print(type(x))

# x = {"name":"ammu","age":10,"place":"kochi","name":"anu"}
# print(x)

# x = {"name":"ammu","age":10,"place":"kochi"}
# print(x["name"])
# print(x["age"])


# x = {"name":"ammu","age":10,"place":"kochi"}
# for i in x: #i is keys
#     print(i)

# for i in x:
#     print(x[i])


# x = {"name":"ammu","age":10,"place":"kochi"}
# print(x.keys())
# print(x.values())
# print(x.items())

# x = {"name":"ammu","age":10,"place":"kochi"}
# for i in x.keys():
#     print(i)

# for i in x.values():
#     print(i)

# x = {"name":"ammu","age":10,"place":"kochi"}
# for i in x.items():
#     print(i)

# x = {"name":"ammu","age":10,"place":"kochi"}
# for i,j in x.items():
#     print(i,j)


# x = {"name":"ammu","age":10,"place":"kochi"}
# x["age"]=20
# print(x)

# x = {"name":"ammu","age":10,"place":"kochi"}
# del x["age"] #key value pair deleted
# print(x)

# del x # dict full deleted


# write a python program to check if value 200 exists in the following dict
# dict1= {"a":100,"b":200,"C":300}
# for i in dict1.values():
#     if i == 200:
#         print("200 exists in the dictionary")
#     else:
#         print("200 not present")

#or
# if 200 in dict1.values():
#     print("200 in dictionary")
# else:
#     print("200 not in dict")

# print("a" in a) true
# print("200" in a) false

# x = {"name":"ammu","age":10,"place":"kochi"}
# print(x['name'])
# z = x.get("name")
# print(z)

# x.update({"name":"anu"})#can update already existing item
# print(x)
# x.update({"course":"python"})#can add item not in dict
# print(x)

# x = {"name":"ammu","age":10,"place":"kochi"}
# y = {"course":"python"}
# x.update(y)

# x = {"name":"ammu","age":10,"place":"kochi"}
# z = x.pop("name")#key which is mentioned will be popped
# print(z)
# print(x)

# z = x.popitem()#last key value pair will be popped
# print(x)

# x = {"name":"ammu","age":10,"place":"kochi"}
# x.clear()
# print(x)

# #1. print the value of key histroy from the below dictionaary
# d = {"class":{"student":{"name":"mike","marks":{"physics":70,"history":80}}}}
# print(d["class"]["student"]["marks"]["history"])

# #or 
# for i in d.values():
#     for j in i.values():
#         for k in j.values():
#             print(k)

# #2. wap to rename a key city to location in the dictionary
# d = {"name":"kelly","age":25,"salary":8000,"city":"newyork"}
# d.popitem()
# y={"loction":"newyork"}
# d.update(y)
# print(d)

# #or
# d = {"name":"kelly","age":25,"salary":8000,"city":"newyork"}
# d["location"] = d.pop("city")
# print(d)

#3. wap to change athira's salary to 8500
# d = {"emp1":{"name":"john","salary":5000},
# "emp2":{"name":"anu","salary":7000},
# "emp3":{"name":"athira","salary":8000}}
# # d["emp3"].update({"salary":8500})
# d["emp3"]["salary"]=8500
# print(d)
 
# #fromkeys method is used  when we need to initialise a dict with  a fixed set of keys and a common value.
# #fromkeys method is used to create a new dict from a given set of keys and a specified value.
# key =["a","b","c"]
# value=[1,2,3] #this is the value that all keys will be assigned
# x = dict.fromkeys(key,value)
# print(x)

# # if not specified default is none
# key =["a","b","c"]
# x = dict.fromkeys(key)
# print(x)

# key =["a","b","c"]
# value=10
# x = dict.fromkeys(key,value)
# print(x)


# my = {"name":"ammu"}
# x = my.setdefault("age",10)
# print(my)

# my = {"name":"ammu"}
# x = my.setdefault("age",None)
# print(my)

# my = {"name":"ammu"}
# x = my.setdefault("name","anu") #name will be ammu itself
# print(my)

# # numbers as keys and its squares as values
# dict1 = {}
# for i in range(1,11):
#     dict1[i]=i*i
# print(dict1)

#d={key:value for i in itreable if condition}
d = {i:i*i for i in range(1,11)}
print(d)

d = {i:i*i for i in range(1,11) if i%2==0}
print(d)

# swap keys and values
d = {"a":1,"b":2,"c":3}#input
# d = {1:"a",2:"b","c":3}#output
d = {j:i for i,j in d.items()}
print(d)

#print dictionary which contains value(age) are even
d ={"ammu":10,"anu":20,"tintu":15,"pinky":25}
d = {i:j for i,j in d.items() if j%2==0}
print(d)

#print dict which contains value(age) are even and greater than 20
d ={"ammu":15,"anu":18,"tintu":35,"pinky":30}
d = {i:j for i,j in d.items() if j%2==0 and j>20}
print(d)

#print dict with value(age) greater than 20 as "old" and less than 20 as young
d ={"ammu":15,"anu":18,"tintu":35,"pinky":30}
d = {i:("old" if j>20 else "young") for i,j in d.items()}
print(d)

#increment everyones salary by 5000
d ={"ammu":15000,"anu":18000,"tintu":35000,"pinky":30000}
d = {i:j+5000 for i,j in d.items()}
print(d)

