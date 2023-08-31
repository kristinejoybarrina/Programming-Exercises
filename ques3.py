# Question 3
# Level 1

# Question:
# With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.
# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

# My own solution

n = 1
num_dict = {}

while n < 9:
    added_dict = {n: n*n}
    num_dict.update(added_dict)
    n += 1
    
print(num_dict) 

# or ANOTHER WAY

n_max = int(input("\nEnter a maximum number that you want to show: "))
num_dict = {}
n = 1

while n < n_max + 1:
    added_dict = {n: n*n}
    num_dict.update(added_dict)
    n += 1
    
print(num_dict) 
