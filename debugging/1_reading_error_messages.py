# You come across the following code. What errors does it raise for the given examples and 
# what exactly do the error messages mean?

def find_first_nonzero_among(numbers):
    for n in numbers:
        if n != 0:
            return n

find_first_nonzero_among(0, 0, 1, 0, 2, 0)
find_first_nonzero_among(1)

# The errors are both TypeErrors - 
# The first one means the numbers given as arguments are more than the number of arguments required
#  by the function and that's what throws the error
# The second TypeError is thrown because the argument 1 is an integer which cannot be iterated over.
