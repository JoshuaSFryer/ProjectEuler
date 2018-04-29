"""
The four adjacent digits in the 1000-digit number that have the greatest product are 9 × 9 × 8 × 9 = 5832.
Find the thirteen adjacent digits in the 1000-digit number that have the greatest product.
What is the value of this product?
"""

with open("problem_8_digits.txt", 'r') as f:
    digitString = f.read()


# Python's replace() method did not seem to be working, so hack fix here to get rid of the newlines
strippedString = str()
for char in digitString:
    if char == "\n":
        pass
    else:
        strippedString += char

lowBound = 0
hiBound = 12

# Tuple format: (Index of first digit in the 13-digit sequence, product)
bestSoFar = (0, 1)

while hiBound <= 1000:
    sample = strippedString[lowBound:hiBound+1]

    product = 1
    for d in sample:
        product *= int(d)

    if product > bestSoFar[1]:
        bestSoFar = (lowBound, product)

    hiBound += 1
    lowBound += 1

print(bestSoFar)
