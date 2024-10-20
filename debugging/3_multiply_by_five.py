# When the user inputs 10, we expect the program to print The result is 50!, but that's not the output we see. 
# Why not?

def multiply_by_five(n):
    return n * 5

print("Hello! Which number would you like to multiply by 5?")
# number = input()
number = int(input())

print(f"The result is {multiply_by_five(number)}!")

# The input from the user will be in the form of a string, so we should see 10 written five times together.
# The input will need to be changed from a string into an integer in order to execute the code as desired.