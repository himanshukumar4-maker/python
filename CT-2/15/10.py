#Question-->Write function to swap 1st and last element of a given tuple.
t=(10,20,30,40,50)
#expected output=(50,20,30,40,10)
def swap(t):
    if len(t)<2:
        return t
    result =(t[-1],)+t[1:-1]+(t[0],)
    return result
print(swap(t))


#Question-->Write a function to rotate a given tuple by K postions.
t=(10,20,30,40,50,60)
k=2
#expected output=(50,60,10,20,30,40)
def rotate(t, k):
    k = k % len(t)
    return t[-k:] + t[:-k]

t = (10, 20, 30, 40, 50, 60)
k = 2

result = rotate(t, k)
print(result)