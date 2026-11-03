str1 = "Orange"

print(len(str1))
print(str1.upper())
print(str1.lower())



str2 = "Apple"

x=str2.find("A")

print(x)


x = str2.replace("A","B")

print(x)

str3 ="Apple"

h = str3.replace("A","")
print(h)



str4 ="Select a Language"
for j in str4:
    if(j.isupper()== True):
    
     print(j.upper())
    else:
     print(j.lower())
     
     #Count each vowels (a,e,i,o,u) for a given strings