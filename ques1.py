# Problem Questions Source: https://github.com/zhiwehu/Python-programming-exercises/blob/master/100%2B%20Python%20challenging%20programming%20exercises.txt


# Question:
# Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence on a single line.

# Pseudocode

# get numbers divisible by 7 with range between 2000 and 3200
num = list(range(1999, 3200))
filtered_nums = []

for n in num:
    
    # remove numbers multiple of 5
    if n % 7 == 0 and n % 5 != 0:
        filtered_nums.append(n)

# display output through a list
print(filtered_nums)



num1 = list(range(1999, 3200))
filtered_nums1 = []

for i in num1:
    if (i%7==0) and (i%5!=0) and (i%2!=0):
        filtered_nums1.append(i)

print (filtered_nums1)

# Best Solution
# Output must be visible by 7 but not in 5, 2, 3 and doesn't end with number 3

num2 = list(range(1999, 3200))
filtered_nums2 = []

for i in num2:
    if (i%7==0) and (i%5!=0) and (i%2!=0) and (i%3!=0) and str(i).endswith("3"):
        filtered_nums2.append(i)

print ("Results:", ', '.join(map(str, filtered_nums2)))      

# Given Solution
l=[]
for i in range(2000, 3201):
    if (i%7==0) and (i%5!=0):
        l.append(str(i))

print (','.join(l))
  

