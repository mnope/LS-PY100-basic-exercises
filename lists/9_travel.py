# Write a function that, without using the built-in in operator, checks whether a specific destination is 
# included within destinations. For example: When checking whether 'Barcelona' is contained in destinations, 
# the expected output is True, whereas the expected output for 'Nashville' is False.

destinations = ['Prague', 'London', 'Sydney', 'Belfast',
                'Rome', 'Aruba', 'Paris', 'Bora Bora',
                'Barcelona', 'Rio de Janeiro', 'Marrakesh',
                'New York City']

def contains(city, lst):
    for place in lst:
        if place == city:
            return True
    return False


print(contains('Barcelona', destinations))  # True
print(contains('Nashville', destinations))  # False
