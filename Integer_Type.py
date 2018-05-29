def integerType(z):
    if z>0:
        print(z,"is +ve Integer")
    elif z<0:
        print(z,"is -ve Integer")
    else:
        print(z,"is zero")
z=int(input("ENTER VALUE OF INTEGER :"))
integerType(z)
