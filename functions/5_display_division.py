# Without running the following code, determine what it will print:

def multiples_of_three():
    divisor = 1

    for dividend in range(3, 31, 3):
        print(f'{dividend} / {divisor} = 3')
        divisor += 1

multiples_of_three

# This code will print nothing because the function call doesn't have parentheses after it and so
# the function is never actually invoked
