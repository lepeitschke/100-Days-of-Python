#Data Types

# String
print("Hello"[0])  #This method is called subscripting. It returns the first character of the string.

print("123" + "456")

#Integer

print(123 + 456)

print(123_456_789)  # returns a large number. The underscore makes it easier to read it.

# Float

print(3.1452)

#Boolean
True
False

#Find out what type the data has.

print(type(1234))

# type conversion

a = float(123)
print(type(a))

# Mathmatical operations
# follow a certain order
# PEMDAS
# () Parentheses
# ** Exponents
# *  Multiplication
# /  Division
# +  Addition
# -  Subtraction

# but in code some characters are equally important from the PEMDAS. 
# ()
# **
# * /
# + -
# If you end up having multiple operators of the same relevance on the same
# line they will be solved from left to right - resulting in the rule PEMDASLR.
print(3*3+3/3-3)    # result 7.7
print(3*(3+3)/3-3)  #result 3.0


# Floor division //
print("Floor division: Results in an integer")
print(8 // 3)

score = 0
height = 1.8
isWinning = True
#f-string
print(f"Your score is {score}, your height is {height}, you are winning {isWinning}.")
