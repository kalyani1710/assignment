n = int(input("Enter the number:"))
def kalyani(n):
    temp=num
    rev=0
    while(num>0):
        tepm=num%10
        rev=rev*10+temp
        num=num//10
    if(temp==rev):
        print("The number is palindrome")
    else:
        print("The number is not a palindrome")  
kalyani(n)              