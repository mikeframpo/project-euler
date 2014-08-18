
import math

def findprimes(n):
    '''return a list containing all the primes up-to and including n.'''
    #trial division method - from en.wikipedia.org/wiki/Prime_number
    
    def isprime(primes, val):
        sqrt = math.sqrt(val)
        for fac in primes:
            # don't need to check any factors above the sqrt of the value
            if fac > sqrt:
                break
            if val % fac == 0:
                return False
        return True

    primes = []
    for val in range(2, n+1):
        if isprime(primes, val):
            primes.append(val)
    return primes

