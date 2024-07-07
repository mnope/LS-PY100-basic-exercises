# What will the following code do and why? Don't run it until you have tried to answer.

b = [1, 2, 3]

def my_function():
    b[0] = 10

my_function()
print(b)

# I think this code will print [10, 2, 3] because while global variables are not able to be modified inside
# of the local scope of a function, the elements of a list are mutable so the variable itself technically
# has not been modified
