#list insert value
list  = [ 5,76,34,"mdshohed"]
print(list)

#value store list last
list.append("desh")
print(list)

list+=["bmw"]
print(list)

#insert function list
list.insert(2,"hello")
print(list)

#list value delete
list = [5,7,3,32,"mdshohed",55]
del list[2]
print(list)

#list value range delete
del list [0:2]
print(list)

list.append(4)
list.append("mdshohed")
print(list)

#delete element in list
list = [ 5,7,6,23,45]
print(list)
newlist = list.pop(2)
print(list, "\n", newlist)

#list value remove

list = [ 5,7,6,23,45]
list.remove(23)
print(list)


#form string to list create
string = "mdsohed", "hello","desh","tararism";
#convert string to list use re library
import  re
list = re.split( ',', string)
print(list)
