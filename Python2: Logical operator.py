

# Logical operator
n = int(input("Enter the value 1: ")) 
m = int(input("Enter the value 2: "))

if  n>=0 and m>=0: 
    print( "Greater then 0")
elif n<=0 and m<=0: 
    print("less then 0")
elif n>=0 or m>=0: 
    print( "n or m greater then 0")
else: 
    print( "")
