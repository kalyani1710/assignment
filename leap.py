x= int(input("Enter the year:"))
def year(y):
    if x % 4==0:
        print(x,"is a leap year")
    else:
        print(x,"is not a leap year")
year(x)            