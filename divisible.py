n = int(input("Enter the sum of all the numbers:"))
def function(n):
    for num in range(n):
        if num % 3 == 0: 
            print((num) + " ",end = " ")
function(n)          