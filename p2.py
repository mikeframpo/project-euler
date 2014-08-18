
#Brute force solution
evensum = 2
fib = [1, 2]

while True:
    fibnext = fib[0] + fib[1]
    fib[0] = fib[1]
    fib[1] = fibnext

    if fibnext >= int(4e6):
        break
    if fibnext % 2 == 0:
        evensum += fibnext

print(evensum)

