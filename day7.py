#A function is defined using the def keyword
def myFun(num):
    num[2] = 10
list = [1, 2, 3, 4, 5]
print(list)
myFun(list)
print(list)

#Arguments are specified after the function name, inside the parentheses. You can add n number of  arguments
def csk(fname):
  print('Player name is' ,fname)
csk("Dhoni")
csk("Raina")
csk("jadaja")

#if your function expects 2 arguments, you have to call the function with 2 arguments, not more, and not less
def ipl(csk_cap,rcb_cap):
  print(csk_cap +' VS '+ rcb_cap)
ipl("India","Pakisthan")

#If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.
def my_function(*team):
  print("The senior member is " + team[0])
my_function("Dhoni", "Raina", "Jadaja")

#You can also send arguments with the key = value syntax & the order of the arguments does not matter.
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)
my_function(child1 = "Dhoni", child2 = "Jadaja", child3 = "Raina")

#If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition.
def my_function(**players):
        print("His last player is "+ players["lplayer"])
my_function(fplayer = "Rayudu", lplayer = "Deepak")

#To let a function return a value, use the return statement:
def my_function(x):
  return 10 * x
print(my_function(10))

#passing a default value while initiation
def csk(fname = "Dhoni"):
  print("Captain for CSK is" + fname)
csk()
