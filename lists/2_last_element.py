# Write a function that returns the last element of a list provided as an argument.

def last(listy):
    if listy:
        return listy[-1]
    else:
        return None


print(last(['Earth', 'Moon', 'Mars']))  # Mars
