"""
Longest Collatz sequence
Problem 14

The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved
yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.

"""
import math

def collatz(n:int):
    chain = list()
    chain.append(n)
    while not n == 1:
        if n % 2 == 0:  # n is even
            n = n // 2  # explicit floor division to avoid floating points in the chain
                        # division occurs only when n is even, so this is not problematic
        else:
            n = 3*n + 1
        chain.append(n)

    return chain


upperBound = 1000000
bestSoFar = (0,0)

"""
Brute force method, checks each of the numbers from 1 to 1 million
Takes about 49.6 seconds on my hardware
for i in range(1, upperBound + 1):
    chain = collatz(i)
    # print(chain)
    if len(chain) > bestSoFar[1]:
        bestSoFar = (i, len(chain))

print(bestSoFar)
"""

# Powers of 2 will just be repeatedly divided by 2
for i in range(1, upperBound + 1):
    # Powers of 2 will just be repeatedly divided by 2, and so will almost assuredly not be the longest chain
    # This saves 20 calls and about 1.8 seconds. Not very much.
    if not math.log(i, 2).is_integer():
        chain = collatz(i)
        if len(chain) > bestSoFar[1]:
            bestSoFar = (i, len(chain))

print(bestSoFar)
