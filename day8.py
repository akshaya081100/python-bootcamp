# Python script to merge two Python dictionaries
dict1 = {'a':10,'b':20,'c':45}
dict2 = {'d':56,'e':99,'f':76}
print("dictionary 1 is",dict1)
print("dictionary 2 is",dict2)
dict1.update(dict2)
print("Merged dictionary is",dict1)

# program to sort the value from descending to ascending in list and convert it in to a set
list1 = [5,17,10,4,8,65,34,93,54]
print("Original list is ",list1)
list1.sort(reverse = True)
print("Descending order",list1)
list1.sort()
print("Ascending order",list1)
s1 = set(list1)
print(s1)

#a Python program to list number of items in a dictionary key and sort the list with the help of a function

dict1 = {'John':90,'Dhoni':83,'Akash':67,'Alan':88}
print("Dictionary is", dict1)
list1 = list(dict1)
print(list1)
list1.sort()
print("Sorted list is",list1)
