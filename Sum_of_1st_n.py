def sumOfN(n):
    sum=0
    for i in range(n+1):
        sum=sum+i
    return print("Sum of first",n,"numbers is",sum)        
n=int(input("Enter limit to print sum of N numbers :"))
sum=sumOfN(n)

