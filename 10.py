
 #Count each vowels (a,e,i,o,u) for a given string.
str8 = "VIJAY GOLD"

a= 0
e = 0
i = 0
o = 0
u = 0

for s in str8:
    if("a" == s or "A" == s):
        a += 1
    elif("e" == s or "E" == s):
        e += 1
    elif("i" == s or "I" == s):
        i += 1
    elif("o" == s or "O" == s):
        o += 1
    elif("u" == s or "U" == s):
        u += 1

print(f"a :{a},e:{e},i:{i},o:{o},u: {u}")
