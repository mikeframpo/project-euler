
sumsquares = 0
sumn = 0
for n in range(1, 101):
    sumsquares += n ** 2
    sumn += n

squaresums = sumn ** 2
print(squaresums - sumsquares)

