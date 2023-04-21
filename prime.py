n = int(input("Enter the prime number in the range:"))
def prime(n):
 for number in range(n):    
    if number > 1:
        for i in range (2 , number):
            if(number % i)== 0:
                break
    else:            
     prime(n)                