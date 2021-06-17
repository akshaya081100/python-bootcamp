#Write a Python script to merge two Python dictionaries

dict1 = {"Maharashtra":"Mumbai", "Telangana":"Hyderabad", "Tamilnadu":"Chennai",}
print("The 1st dictionary is",dict1)
dict2 = {"Karnataka":"Bengaluru", "Bihar":"Patna","Goa":"Panaji"}
print("The 2nd dictionary",dict2)
dict1.update(dict2)
print("Merged dictionary",dict1)


#Write a Python program to remove a key from a dictionary


A = {'a':1 , 'b':2 , 'c':3 ,'d':4 , 'e':5 , 'f':6}
print("Dictionary before change",A)
del A['b']
print("Dictionary after change",A)

# Write a Python program to map two lists into a dictionary

L1 = ['a','b','c','d','e']
L2 = [6,7,8,9,10]
print("List1 is ",L1)
print("List2 is ",L2)
dictionary = {}
for i in L1:
    for j in L2:
        dictionary[i] = j
        L2.remove(j)
        break
print("Final dictionary is",dictionary)

# Write a Python program to find the length of a set

set = {1,2,3,4,5,6,7,8,9,10}
print("The set is ",set)
length = len(set)
print("The length of the set is ",length)

# Write a Python program to remove the intersection of a 2nd set from the 1st set

set1 = {1,2,3,4,5}
print("The set1 is ",set1)
set2 = {10,9,8,6,4,5}
print("The set2 is ",set2)
intersect = set1.intersection(set2)
print("The intersecting elements are",intersect)
set1 -= set2
print("New set1 is",set1)





 
