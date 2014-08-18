

# this is a crude implementation which finds every prime lower than the sqrt
# of the number, then checks whether each value is a prime divisor of the
# number.

# a better implementation, in terms of the fundamental theorem of arithmetic
# would divide the number by each possible prime which is a factor, then
# repetitively divide by the same prime until it is no longer a factor. The
# largest prime factor is achieved when the remaining dividend is unity.

import math

def isprime(primes, val):
    sqrt = math.sqrt(val)
    for fac in primes:
        # don't need to check any factors above the sqrt of the value
        if fac > sqrt:
            break
        if val % fac == 0:
            return False
    return True

def findprimes(n):
    #trial division method - from en.wikipedia.org/wiki/Prime_number
    primes = []
    for i in range(n-1):
        val = i+2
        if isprime(primes, val):
            primes.append(val)
    return primes

num = 600851475143
primes = findprimes(int(math.sqrt(num)))

for prime in reversed(primes):
    if num % prime == 0:
        print(prime)
        break

