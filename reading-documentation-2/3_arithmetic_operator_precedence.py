# 6.17. Operator precedence in Expressions
# https://docs.python.org/3/reference/expressions.html#operator-precedence

result = 4 * 5 + 3**2 / 10  
# result = 4 * 5 + 9 / 10       # exponentiation
# result = 20 + 0.9             # multiplication and then division, from left to right
# result = 20.9                 # addition
print(result)
