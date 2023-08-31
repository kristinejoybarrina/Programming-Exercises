# Question 2
# Level 1

# Question:
# Write a program which can compute the factorial of a given numbers.
# The results should be printed in a comma-separated sequence on a single line.
# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# 40320


# Using math module

import math

input_num = int(input("Enter a number: "))
factorial_num = math.factorial(input_num)

print(f"The factorial of {input_num} is {factorial_num}")


# Without using module, based on factorial formula

input_num = int(input("Enter a number: "))
factorial_num = 1

for i in range(1, input_num+1):
    factorial_num *= i
    
print (factorial_num)


# Given solution
def fact(x):
    if x == 0:
        return 1
    return x * fact(x - 1)

input_num = int(input("Enter a number: "))
result = fact(input_num)
print(result)
