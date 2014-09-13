
import util
import math

n = 10001

pi_block = 1000

# the PNT gives us a decent first guess to sieve through.
pi = int(n * math.log(n))

primes = util.prime_sieve(n)

while len(primes) < n:
    pi += pi_block
    primes = util.findprimes(pi, primes)

print(primes[n-1])

