"""
Largest prime factor
Problem 3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

"""

def primeBreakdown(n:int):
    """
    Trial division implementation. Based on the implementation found on Wikipedia at:
    https://en.wikipedia.org/wiki/Trial_division

    For the sake of memory conservation if nothing else, this method uses a set instead of a list of factors.
    Thus, it ignores duplicate factors (i.e. while there will likely be many instances of 2 and 3 as factors,
    they won't be counted separately. We only want the unique factors to find the largest of them, so this is fine.
    """

    factors = set()
    divisor = 2

    while n > 1:
        # If the number is divisible by the divisor, then it's a factor. Divide the number by it and continue decomposing
        if (n % divisor) == 0:
            factors.add(divisor)
            n = n / divisor

        else:
            # Indivisible by the current divisor, so try the next possible one
            divisor += 1
    return factors

print("The largest prime factor of 600851475143 is " + str(max(primeBreakdown(600851475143))))




