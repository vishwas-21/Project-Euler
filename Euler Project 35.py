import math


def isPrime(n):
    if n > 0:
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True
    return False

def isCirculerPrime(n):
    string = str(n)
    length = len(string)
    for i in range(length):
        if not isPrime(n):
            return False
        string = string[1:] + string[0]
        n = int(string)
    return True

count = 0
for i in range(2, 1000000):
    if isCirculerPrime(i):
        count += 1
        print(i)

print(count)

