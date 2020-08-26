import math


def isPrime(n):
    if n == 1:
        return False
    if n > 0:
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

def ispermutation(n, num):
    temp = str(n)
    ori = [int(x) for x in temp]
    temp = str(num)
    per = [int(x) for x in temp]
    ori.sort()
    per.sort()
    if ori == per:
        return True
    return False

"""
    Remember Answer Should be written increasing order
"""

def checkperprop(n):
    temp = str(n)
    num = [x for x in temp]
    for e1 in num:
        num1 = num.copy()
        num1.remove(e1)
        for e2 in num1:
            num2 = num1.copy()
            num2.remove(e2)
            for e3 in num2:
                num3 = num2.copy()
                num3.remove(e3)
                per = int(e1 + e2 + e3 + num3[0])
                if isPrime(per) and n != per:
                    temp = max(per, n) - min(per, n) + max(per, n)
                    if isPrime(temp):
                        if ispermutation(n, temp):
                            print(n, temp, per)
                            quit()
                    temp = max(per, n) - min(per, n)
                    temp = min(per, n) - temp
                    if isPrime(temp):
                        if ispermutation(n, temp):
                            print(n, temp, per)
                            quit()

for i in range(1000, 10000):
    if isPrime(i) and i != 1487 and i != 4817 and i != 8147:
        checkperprop(i)
    print(i)
