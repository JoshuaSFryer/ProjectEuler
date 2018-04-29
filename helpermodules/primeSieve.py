"""
This implements the Sieve of Eratosthenes, searching for all primes from 2 - 100 000. If the 10001st prime is not
found within this range, it continues searching between 2 - 200 000, and so on
"""

def eratosthenes(bound:int):

    # Working with an array of booleans for marking is better than using a dictionary as originally planned
    # Since the keys are simply consecutive integers, might as well use array indices.

    # Make an array of booleans, representing the integers from 0 to bound.
    max = bound + 1
    nums = [True] * (max)
    p = 2
    endReached = False

    while not endReached:
        # Flag the multiples of P, starting from 2P. These are, by definition, not prime numbers
        for i in range(2*p, max, p):
            nums[i] = False

        # I wish python had a do-while loop, but since it does not, we get this ugly little block

        # Increment P if it is safe to do so
        if p >= bound:
            endReached = True
        else:
            p += 1

        # Search for the next unflagged number and use it as the next P
        while (nums[p] is False) or p == 2:
            if p >= bound:
                endReached = True
                break
            else:
                p += 1

    primes = list()
    # Store all the unflagged (i.e. prime) numbers into a list
    for i in range(2, bound):
        if nums[i] is True:
            primes.append(i)
    print(str(len(primes)) + " prime numbers found between 2 and " + str(bound))
    return (primes)
