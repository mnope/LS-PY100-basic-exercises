# What will the following code do and why? Don't run it until you have tried to answer.

a = 7

def my_function(b):
    b += 10

my_function(a)
print(a)

# I think this code will print 7 because a is being passed as an argument to the function, but
# not modified directly by it. my_function has no return or print statement so it will have no output
