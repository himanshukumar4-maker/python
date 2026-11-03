#count all the numbers from 1 to n which are divisible by 5&3.

n=int(input("Enter a number n;"))
i = 1
while(i<=n):
    if(i%3==0 and i%5==0):
        print(i)
    i+=1