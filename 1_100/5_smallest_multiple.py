"""
Smallest multiple
Problem 5

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

"""

# No solutions were found between (20 * 19) and 10^9, so starting from here
testNum = 10**9

# We only need to check primes and the most composite numbers (i.e. if we check 18, we don't need to check 2, 9, 3, 6)
numsToCheck = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11]

multples = list()

while testNum < 10 ** 11:
    isMultiple = True
    for divisor in numsToCheck:
        if testNum % divisor != 0:
            isMultiple = False

    if isMultiple:
        multples.append(testNum)
        print("solution found: " + str(testNum))

    testNum += 1


print(multples)

# putting this one on hold for now. Returned 1163962800 which Proj. Euler says is incorrect. Will have to revise
# and make more efficient for easier testing.
