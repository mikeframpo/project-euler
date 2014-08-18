
def checkpalendrome(dig):
    for idig in range(len(dig)):
        if dig[idig] != dig[-(idig+1)]:
            return False
    return True

digits = 3
highest = -1

for i in reversed(range(1, 10 ** digits)):
    for j in reversed(range(1, i+1)):
        mult = i * j
        if highest > mult:
            continue
        dig = []
        # the multiple of two 3 digit numbers is at most a 6 digit number
        multtmp = mult
        for idig in reversed(range(digits * 2)):
            digval = multtmp / (10 ** idig)
            dig.append(digval)
            multtmp -= digval * (10 ** idig)

        while dig[0] == 0:
            dig.pop(0)

        if checkpalendrome(dig):
            highest = mult

print(highest)

