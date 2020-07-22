import math

def isPrime(n):
    if n == 1:
        return False
    elif n > 0:
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True
    return False


def truncatableLandR(n):
    string = str(n)
    while len(string) > 0:
        if isPrime(int(string)):
            string = string[1:]
        else:
            return False
    string = str(n)
    while len(string) > 0:
        if isPrime(int(string)):
            string = string[:-1]
        else:
            return False
    return True

count = 0
sumTrunc = 0
i = 10
while count < 11:
    if truncatableLandR(i):
        count += 1
        sumTrunc += i
        print(i)
    i += 1

print("Sum is", sumTrunc)