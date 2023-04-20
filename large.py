n1=10
n2=20
n3=30
def largest(n1,n2,n3):
 if(n1>n2) and (n1>n3):
    print("the largest number is",n1)
 elif (n2>n1) and (n2>n3):
    print("the largest number is",n2)
 else: 
    print("the largest number is",n3)
largest(n1,n2,n3)       
