a = {1,2,3,4,5}
print(a)
print(type(a))
print(len(a))

p = {"python","java","java",10,20,10,20}
print(p)
print(len(p))#duplicates will not come

p = {"python","java",10,20}
print(p)#no order

y={True,10,20,"java",0,"php",False,1}
print(y) #0=False,1=true

#set methods----------------------------------------

y = {"python","java",10,20}
print(dir(y))

p = {"python","java",10,20}
p.add("orange") #add method is used to add items to set
print(p)

p.update(y)
print(p)

p = {"python","java",10,20}
k=[10,20,30]
p.update(k)
print(p) #update is used to add tuple or list items to set

#remove and discard are same only difference is when item is not in the set
p={"python","java",10,20}
p.remove("java")
print(p)

p={"python","java",10,20}
p.discard("python")
print(p)

p={"python","java",10,20}
p.remove("abc")
print(p)#abc is not in set so error will be printed

p={"python","java",10,20}
p.discard("abc")
print(p)#abc is not in set but the set will be printed as such

p={"python","java",10,20}
p.clear()#output will be set()
print(p)


p = {"python","java","hai","hello"}
q = {"php","dotnet","hai","hello"}
x = p.union(q)#union of both p &q . no repeated
print(x)
print(p|q)

p = {"python","java","hai","hello"}
q = {"php","dotnet","hai","hello"}
x = p.intersection(q)#common
print(x)
print(p&q)
p.intersection_update(q)
print(p)#intersection update will change the original set instead of returning a new set.same as diff but ans will be updated to p itself
p&=q
print(p)

p = {"python","java","hai","hello"}
q = {"php","dotnet","hai","hello"}
x = p.difference(q) #present in p not in q
x = q.difference(p) #present in q not in p
print(x)
print(q-p)
p.difference_update(q)
print(p)
p-=q
print(p)

p = {"python","java","hai","hello"}
q = {"php","dotnet","hai","hello"}
x = p.symmetric_difference(q)#items other than common
print(x)
print(p^q)
p.symmetric_difference_update(q)
print(p)
p^=q
print(p)

#for loop
p = {"python","java","hai","hello"}
for i in p :
    print(i)

#for i in range is not possible

p = {"python","java","hai","hello"}
y = p.pop()#any item will be popped since no index any item will be removed
print(p)
print(y)

numbers = {1,2,3,4,5,6,7,8,9,10}
odd = {1,3,5,7,9}
even = {2,4,6,8,10}
print(numbers.issuperset(odd))
print(numbers.issuperset(even))
print(odd.issuperset(even))
print(odd.issubset(even))
print(odd.issubset(numbers))
print(odd.isdisjoint(even))# isdisjoint checks whether 2 sets have a intersection or not

odd = {1,3,5,7,9}
p=odd.copy()
print(p)

#1. WAP to add all elements in list1 into given set
set1 = {"yellow","orange","black"}
list1 = ["blue","green","red"]
set1.update(list1)
print(set1)

#2 return a  new set of identical items frm 2 sets
set1 = {10,20,30,40,50}
set2 = {30,40,50,60,70}
x = set1.intersection(set2)
print(x)

#3. get only unique items from 2 sets
set1 = {10,20,30,40,50}
set2 = {30,40,50,60,70}
x = set1.symmetric_difference(set2)
print(x)

#4. update the 1st set with items that dont exist in the 2nd set
set1 ={10,20,30}
set2 = {20,40,50}
set1.difference_update(set2)
print(set1)

#5. return a set of elements present in set1 a or set2 but not both
# set1 = {10,20,30,40,50}
# set2 = {30,40,50,60,70}
set1 = {10,20,30,40,50}
set2 = {30,40,50,60,70}
x = set1.symmetric_difference(set2)
print(x)
