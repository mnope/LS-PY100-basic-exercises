# What will the following code do and why? Don't run it until you have tried to answer.

a = 1

def my_function():
    global a
    a = 2

my_function()
print(a)

# I think this code will print 2 because we have used the global keyword to modify the global variable
# inside the local scope of the function definition
