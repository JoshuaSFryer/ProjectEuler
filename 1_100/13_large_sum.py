"""
Large sum
Problem 13

Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
[See problem_13_data.txt]
"""
with open("problem_13_data.txt") as f:
    lines = f.readlines()

nums = list()
for line in lines:
    nums.append(int(line))

"""
Simplest, brute force method: Just add them all up
"""

sum = 0
for number in nums:
    sum += number

# Convert to string and take the first ten digits
sumString = str(sum)
firstTen = sumString[0:10]
print(firstTen)