"""
10001st prime
Problem 7

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""

from helpermodules import primeSieve

# Initial search bounds
testRange = 100000

while True:
    primeList = primeSieve.eratosthenes(testRange)

    # If the 10001st prime has not been found, expand the search range
    if len(primeList) < 10001:
        testRange *= 2

    # Otherwise, we have our solution and simply need to extract it
    else:
        print("The 10001st prime number is " + str(primeList[10000]))
        break
