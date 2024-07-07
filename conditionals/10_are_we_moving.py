# Determine what the following code snippet prints. 
# First solve it in your head or on paper, then run it in your Python environment to check the result.

speed = 0
acceleration = 24
braking_force = 19
is_moving = braking_force < acceleration and (speed > 0 or acceleration > 0)
print(is_moving)

# prints True


# Bonus question: Do we need the parentheses in the boolean expression or could we have written the following?:
is_moving = braking_force < acceleration and speed > 0 or acceleration > 0

# Technically I thnk this one would've evaluated correctly still, but the parentheses are necessary because
# and has higher priority than or in evaluating statements and that may not always provide the desired outcome