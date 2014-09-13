
import math

def findprimes(n, primes=None):
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

    if primes is None:
        start = 2
        primes = []
    else:
        start = primes[-1] + 1
        assert n > primes[-1]
    
    for val in range(start, n+1):
        if isprime(primes, val):
            primes.append(val)
    return primes

def prime_sieve(n):
    isprime = [True] * (n-1)
    for p in range(2, n+1):
        for pmult in range(2, n/p + 1):
            isprime[(p * pmult) - 2] = False
    return [i+2 for i in range(len(isprime)) if isprime[i]]

