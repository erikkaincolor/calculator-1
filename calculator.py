"""CLI application for a prefix-notation calculator."""

from arithmetic import *
#the asterisk imports functions from arithmetic


#https://fellowship.hackbrightacademy.com/materials/wmt5/exercises/calculator-1/solution/index.html



#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^#
#the program is EXPLICITLY prefix arithmetic bc the conditionals are set to expect the token 
# list item at index 0 to be the operator string....
# operator string is designed here to dictate the function. if i enter "1 + 1" is gives error 
# bc token[0] is a number instead of a operaor string as explicitly stated
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^#


#these "inputs" are almost like arguments....

#why is this API built all funky like this? 
#if -break-, elif -continue-
#if, else, if, if not -continue-, elif, elif, elif, elif, elif, elif, else

while True:
    user_input = input("Enter your equation > ") #assigned input to var
    tokens = user_input.split(" ")               #reassigned input to variable thatll return a seperated list of string inputs

    if "q" in tokens:                           #these inputs seem to be player controls almost, q= quit
        print("You will exit.")                 #if q is in list of inputs
        break

    elif len(tokens) < 2:                       # if amount (in length) of inputs are way too little
        print("Not enough inputs.")
        continue

    operator = tokens[0]                        # variable for first input via index list
    num1 = tokens[1]                            # variable for second input via index list

    if len(tokens) < 3:                         # if amount (in length) of inputs are too little
        num2 = "0"

    else:
        num2 = tokens[2]

    if len(tokens) > 3:                          #need num3 as a parameter in function def
        num3 = tokens[3]                       

    # A place to store the return value of the math function we call,
    # to give us one clear place where that result is printed.
    result = None

    if not num1.isdigit() or not num2.isdigit():        #if num1 or num2 is not a int
        print("Those aren't numbers!")
        continue

    # We have to cast each value we pass to an arithmetic function from a
    # a string into a numeric type. If we use float across the board, all
    # results will have decimal points, so let's do that for consistency.

    elif operator == "+":
        result = add(float(num1), float(num2))

    elif operator == "-":
        result = subtract(float(num1), float(num2))

    elif operator == "*":
        result = multiply(float(num1), float(num2))

    elif operator == "/":
        result = divide(float(num1), float(num2))

    elif operator == "square":
        result = square(float(num1))

    elif operator == "cube":
        result = cube(float(num1))

    elif operator == "pow":
        result = power(float(num1), float(num2))

    elif operator == "mod":
        result = mod(float(num1), float(num2))

    elif operator == "x+":                                              ##need function def
        result = add_mult(float(num1), float(num2), float(num3))

    elif operator == "cubes+":                                          #need function def
        result = add_cubes(float(num1), float(num2))

    else:
        result = "Please enter an operator followed by two integers."

    print(result)
