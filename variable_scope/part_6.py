# What will the following code do and why? Don't run it until you have tried to answer.

a = 1

def my_function():
    a = 2

my_function()
print(a)

# I think this code will throw an Undefined Local Variable error and then print 1

# I was wrong about the error on this exercise because prior to this I did not understand that you could
# have an identical variable in the global and again in a local scope at all
