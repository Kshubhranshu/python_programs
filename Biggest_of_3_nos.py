def Biggest(a,b,c):
    if a>b and a>c:
        print(a,"is biggest of three")
    elif b>a and b>c:
        print(b,"is biggest of three")
    else:
        print(c,"is biggest of three")
a,b,c = input("Enter three numbers :").split()
Biggest(int(a),int(b),int(c))

        
            
    
              
            
    
