a=[1,2,3,4,5,6,7,8,9,10,11,12,13]
a.append(14)
print("Append :",a)

b=a.count(4)
print("Count :",b)

c=[15]
a.extend(c)
print("Extend :",a)

d=a.index(5)
print("Index :",d)

a.insert(7,7.5)
print("Insert :",a)

a.pop(7)
print("Pop :",a)

a.remove(15)
print("Remove :",a)

del a[0:14:2]
print("Delete :",a)

e=len(a)
print("Length :",e)

f=min(a)
print("Minimum :",f)

g=max(a)
print("Maximum :",g)

a=[1,2,3,4,5,6,7,8,9,10,11,12,13]
h=sum(a)
print("sum of (a) :",h)

a.reverse()
print("Reverse :",a)
