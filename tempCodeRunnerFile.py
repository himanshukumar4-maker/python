list1 = [10,20,30,40,50,60,70,80,90,100]
list2 = ["Rungta",0.9,False,77]
print(list1)

tuple1 = (10,20,30,40,50,60,70,80,90,100)
print(tuple1)

print(max(list1))
print(max(list1))

print(min(list1))
print(sum(list1))
list1.append(110)
print(list1)
# insert's an element at particular position
print(list1.insert(6,55))
print(list1)
print(list1.count(40))
print(list1.index(60))


li3 = [i for i in range(1,11)]
print(li3)

li4 = [i for i in range(50,101) if i%2==0]
li6 = [78,99,1010,li4,5.0]
for i in range(len(li6)):
    print(li6[i])
    
for i in li6:
    print(i)    


#tuple unpacking
st5 = ("Ravi",21,86)
name,age,per_st5= st5 
print(name)
print(age)
print(per_st5)

a=10
b=20
a,b=b,a

print(a)
print(b)

li=[1,2,2,3]
t1=(5,56,6,7)

print(tuple(li))
print(type(tuple(li)))
print()
print(list(t1))
print(type(list(t1)))

#Create a new list from an pre-existing tuple,
# where each of the new elements of list should the cube of the elements of tuple if and only if the elements are odd.
t2=(56,67,99,87,31,32)
li_new=[i**3 for i in t2 if i%2 !=0]
print(li_new)
li_new=[i**3 for i in t2 if i%2 !=0]

