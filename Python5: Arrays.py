# list int value input
list = []
n = int(input())
for i in range(0, n):
    t = int(input())
    list.append(t)
print(list)

# list string value input
list2 = []
p = int(input())
for i in range(0, p):
    t = str(input())
    list2.append(t)
print(list2)

list = 
# 2d matrix represent
matrix = [[1, 3, 4, 5], [2, 4, 6, 8], [1, 5, 9, 2],[5, 9, 54, 23]]
for i in matrix:
    for j in i:
        print(j)
    print()

for i in matrix:
    for j in i:
        print(j, end=' ')
    print()

print(matrix[0:2]);

# ara search found after that new string add
ara = ["mdshohed", "hello", "tusar", "anti"];
for car in ara:
    print(car)
    if car == "hello":
        print("hello mutu")

# sum calculate int or not


list = [2, 3, 4, "mdshohed", 5]
sum = 0
for i in list:
    if type(i) == int:
        sum += i
print("sum is : {sum}".format(sum=sum))
