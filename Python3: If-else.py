# Mark calculate
mark = int(input("Enter exam mark: "))

if mark >= 80:
    print("A+")
elif mark >= 75:
    print("A-")
elif mark >= 70:
    print("A")
elif mark >= 65:
    print("B+")
elif mark >= 60:
    print("B-")
elif mark >= 55:
    print("B")
elif mark >= 50:
    print("B-")
elif mark >= 45:
    print("C")
elif mark >= 40:
    print("D")
else:
    print("F")

# even odd
value = int(input("Enter the value: "))
if value % 2 == 0:
    print("Even\n")
else:
    print("Odd\n")
    
    
# Ternary Operator
a = 100
b = 50
print(a if a > b else b)
