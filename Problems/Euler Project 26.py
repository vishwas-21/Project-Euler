def recurringLength(string):
    maxLength = 0
    i = 0
    while True:
        string = string[1:]
        if string.count(string[0] if len(string) > 0 else "____") > len(string) - 2:
            maxLength = 1
            break
        for j in range(1, len(string)):
            if string[0] == string[j]:
                if string[:j] == string[j:2 * j] == string[2 * j : 3 * j]:
                    maxLength = j

                    break
        else:
            continue
        break
    return maxLength

from decimal import *
getcontext().prec = 5000
maxNum = 0
for n in range(2, 1001):
    test = str(Decimal(1) / Decimal(n))
    test = test[2:]
    i = 0
    temp = recurringLength(test)
    if maxNum < temp:
        maxNum = temp
        element = n
    n += 1
print(element)