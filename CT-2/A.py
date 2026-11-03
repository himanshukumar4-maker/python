# n= 10

# for i in range(1,n+1):
#     if i ==4:
#         break
#     print(i)
# print("Hello")    


# n= 10

# for i in range(1,n+1):
#     if i ==4:
#         continue
#     print(i)
# print("Hello")    





# #print all the odd numbers from 1 to n using break/continue
    
# x= 10
# for i in range (1,n+1):
#     if i%2==0:
#         continue
#     print(i)
# print("Hello")    
    
    
    
#Print number of ways to reach on the top stairs if input is given as total no. of stairs.

#hint--> only take 1 or 2 steps at a time.
#solution--> no. of ways to reach on top by 1-step.[{1},{2} for two stairs]

#To find the number of ways to reach by 1 or 2 steps at a time.

# n = int(input())
# def f (n):
#     if n==1:
#         return 1
#     if n==2:
#         return 2
#     return f(n-1) + f(n-2)
# print (f(n))

# #if f(5)
#  ____ ___|______
#  |             |
#   f(4)       f(3)
 
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      # question 1.print the sum of all the numbers from 1 to n using recursion.
 
# n=int(input("Enter n :"))

# result= "recursive_sum"(n)
# print(f" The sum of numbers from 1 to {n} is: {result}")
     
     
     
     
     
     
      # question 2. calculate a^b using recursion only and do not use ** or pow()
      
# def f(a,b):
#     if b==0:
#         return 1
#     return a * f(a,b-1)
# print(f(2,5))      
      
      
      
      
#Check whether a number is an armstrong number using recursion.      
def armstrong(n, original, power):
    if n == 0:
        return 0
    return(n%10)** power+armstrong(n//10)


num = int(input("Enter a number: "))

power = len(str(num))

if armstrong(num, num, power) == num:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")    