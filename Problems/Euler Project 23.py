import math


def propDivisors(n):
    sumProp = 1
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            if i != n // i:
                sumProp += (i + n // i)
            else:
                sumProp += i
    return sumProp


def isAbundant(n):
    return propDivisors(n) > n


total = [n + 1 for n in range(28123)]
sumt = sum(total)
abundant = []
for i in range(2, 28124):
    if isAbundant(i):
        abundant.append(i)

k = 0
print(abundant)
for i in abundant:
    for j in abundant[abundant.index(i):]:
        if i + j <= 28123:
            if i + j in total:
                total.remove(i + j)
        else:
            break
    print(k)
    k += 1

print(sum(total))
