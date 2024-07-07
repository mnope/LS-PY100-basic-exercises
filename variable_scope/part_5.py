# What will the following code do and why? Don't run it until you have tried to answer.

a = 1

def my_function():
    print(a)
    a = 2

my_function()

# I think this code will print 1 and then throw an error because you cannot reassign a global variable
# inside a function without the global keyword

# I was wrong on this one because I think python will read the whole function definition prior to executing
# any code in it and so would see that a was unable to be reassigned and so was undefined before printing 1
