
import math
import util

N = 1000

for b in range(1,N-1):
    num = N*(N - 2*b)
    den = 2*(N - b)
    a = num/den
    if a*den != num:
        #a not integer
        continue
    if a < 0 or a >= N:
        continue
    c = N-a-b
    print('vals: %d, %d, %d' % (a, b, c))
    print('prod: %d' % (a*b*c))

