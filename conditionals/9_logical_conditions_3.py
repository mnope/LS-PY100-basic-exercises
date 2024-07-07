# Without running the following code, determine what will be printed.

sale = True
admission_price = 5.25 if not sale else 3.99

print(f"${admission_price}")

# I think '$3.99' will be printed because 'not sale' will evaluate to False as sale is True
