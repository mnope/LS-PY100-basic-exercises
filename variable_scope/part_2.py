# What will the following code do and why? Don't run it until you have tried to answer.

x = 10

def my_function():
    x = x + 5
    print(x)

my_function()

# I think this code will throw an error because you can't reassign a global variable inside a function
# and x is not defined inside the function
