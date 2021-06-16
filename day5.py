#Write a program to create a list of n integer values and do the following
#Add an item in to the list (using function)
#Delete (using function)
#Store the largest number from the list to a variable
#Store the Smallest number from the list to a variable

list=[1,2,3,4,5,6,7,8,9,10]
print("The list is",list)
largenum = max(list)
print("The largest number is",largenum)
smallnum = min(list)
print("The smallest number is",smallnum)

b = list.append(11)
print("The list after appending",list)

list1 = ['A' ,'B','C','D']
del list1[3]
print("The list after deletion",list1)

#Create a tuple and print the reverse of the created tuple

tuple = (1, 2, 3 , 7 ,10,43)

print("The initial tuple is",tuple)
new = sorted(tuple,reverse = True)
print("The reversed tuple is",new)

#Create a tuple and convert tuple into list

tuple = (1, 2.5, 'hello' , 'world' , 65, 24)
print("tuple is",tuple)
list_new = list(tuple)
print("List is",list_new)

