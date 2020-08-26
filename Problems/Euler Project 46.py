import math

def isPrime(n):
    if n > 0:
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True
    return False

def isTwiceOfSquare(n):
    if n % 2 == 0:
        n = n // 2
        temp = math.sqrt(n)
        if int(temp) == temp:
            return True
    return False

def checkConjecture(n):
    for i in range(2, n - 1):
        if isPrime(i):
            if isTwiceOfSquare(n - i):
                return True
    return False

i = 2
while i:
    if i % 2 != 0:
        if not isPrime(i):
            if not checkConjecture(i):
                print("Answer is", i)
                quit()
    i += 1
    print(i)