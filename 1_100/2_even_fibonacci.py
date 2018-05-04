"""
Even Fibonacci numbers
Problem 2

Each new term in the Fibonacci sequence is generated by adding the previous two terms.
By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million,
find the sum of the even-valued terms.
"""
import math

"""
# The recursive implementation is disgustingly inefficient at computing larger fibonacci numbers 
# (complexity O(2^n) means that on my hardware, n = 40 takes over 100 seconds and n = 41 takes 163).
def fibonacci(n):
    # print(n)
    if n == 0:
        return 1
    elif n == 1:
        return 2
    else:
        return fibonacci(n-1) + fibonacci(n-2)
"""

# Iterative method should be O(n)
def fibonacci(n):
    if n <= 1:
        return n

    else:
        curr = 1
        prev = 1
        for i in range (2, n):
            temp = curr
            curr += prev
            prev = temp

        return curr

"""
The golden-ratio approach to finding the fibonacci numbers is probably faster, especially on Intel machines
that have a native SQRT instruction (assuming that C, and by extension Python, make use of this fact).

Regardless, it's O(1), and so should be faster anyway.
"""
goldenRatio = (1 + math.sqrt(5))/2


def fibGolden(n):
    return int((goldenRatio ** n - (1-goldenRatio)**n)/math.sqrt(5))


# determine which fibonacci number has a value of 4 million or greater
count = 0
fib = 0
while fib <= 4000000:
    count += 1
    fib = fibGolden(count)

sumOfEvens = 0
for i in range(0, count):
    term = fibGolden(i)
    if term % 2 == 0:
        sumOfEvens += term

print("The sum of the first " + str(count) + " even Fibonacci numbers is " + str(sumOfEvens))
