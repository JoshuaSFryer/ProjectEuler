"""
Largest palindrome product
Problem 4

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""


def isPalindrome(n: int):
    string = str(n)
    # Split up the string into strings containing individual digits
    original = list(string)
    # Make an empty list to reverse the string into
    stack = list()
    # 'reversed' makes a backwards iterator over the string
    for digit in reversed(original):
        stack.append(digit)

    backwards = ""
    # Put the reversed digits back into a string
    for digit in stack:
        backwards += digit

    return int(backwards) == n


largestSoFar = 0
for i in range(999, 100, -1):
    for j in range(999, 100, -1):
        product = i * j
        if isPalindrome(product):
            if (product) > largestSoFar:
                largestSoFar = product

print("The largest palindromic product from two 3-digit numbers is " + str(largestSoFar))