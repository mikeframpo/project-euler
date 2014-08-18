
import util

if False:
    # brute force solution
    def checkdivisors(val):
        for i in range(1, 21):
            if val % i != 0:
                return False
        return True

    num = 20
    while True:
        if checkdivisors(num):
            print(num)
            break
        num += 20

if True:
    # better solution, decomposing each number from 1-20 into it's composite
    # primes and then multiplying together to form a number which contains
    # all decompositions of the numbers 1-20.
    num = 20
    primes = util.findprimes(num)

    def decompose(n, primes):
        decomp = {}
        for prime in primes:
            while n % prime == 0:
                n /= prime
                if not decomp.has_key(prime):
                    decomp[prime] = 1
                else:
                    decomp[prime] += 1
            if n == 1:
                break
        assert n == 1
        return decomp

    primeset = {}
    for n in range(2, num+1):
        decomp = decompose(n, primes)
        for prime in decomp.iterkeys():
            if not primeset.has_key(prime):
                primeset[prime] = decomp[prime]
            else:
                primeset[prime] = max(primeset[prime], decomp[prime])

    mindivisor = 1
    for prime in primeset.iterkeys():
        mindivisor *= prime ** primeset[prime]

    print(mindivisor)

