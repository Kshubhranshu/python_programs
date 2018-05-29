def palindrome(n):
    while(n/10 != "null"):
        temp=n%10
        temp=chr(temp)
        new_number+=temp
        n/10;
    if s==new_number:
        print("is Palindrome")
    else:
        print("is Not Palindrome")
    return
s=input("Enter a number :")
n=int(s)
palindrome(n)
