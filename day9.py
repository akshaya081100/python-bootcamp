#To add +2to every element in the list
list = [1,2,3,4,5,6,7,8]
print("The list is",list)
newlist = []
for i in list:
    newlist = i+2
    print(newlist)

# To print the 5,4,3.. pattern
for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print(j, end="")
    print()


    
#Python program to generate Fibonacci series until 'n' value
 nterms = int(input("How many terms? "))

# first two terms
n1, n2 = 0, 1
count = 0

# check if the number of terms is valid
if nterms <= 0:
   print("Please enter a positive integer")
# if there is only one term, return n1
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
# generate fibonacci sequence
else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(n1)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1   

  
#To generate armstrong number
  # Python program to check if the number is an Armstrong number or not

# take input from the user
num = int(input("Enter a number: "))

# initialize sum
sum = 0

# find the sum of the cube of each digit
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10

# display the result
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")


#To print the multiplication of 9

num = int(input(" Enter the number : "))    
# using for loop to iterate multiplication 10 times     
print("Multiplication Table of : ")  
for i in range(1,11):    
   print(num,'x',i,'=',num*i) 



#To check the program positive or negative
   num = float(input("Enter a number: "))  
  
if num > 0:  
 print("{0} is a positive number".format(num))  
elif num == 0:  
   print("{0} is zero".format(num))   
else:  
   print("{0} is negative number".format(num))   



    
    
# To convert days into ages
days= int(input("Enter the number of days"))
years= days / 365  
print("Number of years is: ");  
print(years);  




#To solve trignomertic function using math function
# importing math module
import math

# number 
x = 0.75

# math.cos()
print("math.cos(",x,"): ", math.cos(x));
# math.sin()
print("math.sin(",x,"): ", math.sin(x));
# math.tan()
print("math.tan(",x,"): ", math.tan(x));

# math.acos()
print("math.acos(",x,"): ", math.acos(x));
# math.asin()
print("math.asin(",x,"): ", math.asin(x));
# math.atan()
print("math.atan(",x,"): ", math.atan(x));

y = 2
# math.atan2(y,x) = atan(y/x)
print("math.atan2(",y,",",x,"): ", math.atan2(y,x))

# math.hypot(x,y)
print("math.hypot(",x,",",y,"): ", math.hypot(x,y))



# To create calculator

# menus
print("Calculator")
print("1.Add")
print("2.Substract")
print("3.Multiply")
print("4.Divide")

# input choice
ch=int(input("Enter Choice(1-4): "))

if ch==1:
    a=int(input("Enter A:"))
    b=int(input("Enter B:"))
    c=a+b
    print("Sum = ",c)
elif ch==2:
    a=int(input("Enter A:"))
    b=int(input("Enter B:"))
    c=a-b
    print("Difference = ",c)
elif  ch==3:
    a=int(input("Enter A:"))
    b=int(input("Enter B:"))
    c=a*b
    print("Product = ",c)
elif ch==4:
    a=int(input("Enter A:"))
    b=int(input("Enter B:"))
    c=a/b
    print("Quotient = ",c)
else:
    print("Invalid Choice")
