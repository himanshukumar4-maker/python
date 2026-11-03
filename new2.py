#Write a function to print all the digits of a given number {n=7369}
n=int(input())
print()
def dp(n):
    while(n!=0):
        ld=n%10
        print(ld)
        n=n/10
        
dp(n)

