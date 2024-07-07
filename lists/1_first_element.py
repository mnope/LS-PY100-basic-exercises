# Write a function that returns the first element of a list provided as an argument.


def first(listy):
    if listy:
        return listy[0]
    else:
        return None


print(first(['Earth', 'Moon', 'Mars']))  # Earth
