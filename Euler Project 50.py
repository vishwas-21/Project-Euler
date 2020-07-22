import math

def isPrime(n):
    if n > 0:
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True


i = 2
n = 1000000
sumPrimes = [0]
length = 0
primes = []
while True:
    if isPrime(i):
        primes.append(i)
        for j in range(len(primes)):
            tempSum = sum(primes[j:])
            if isPrime(tempSum):
                if tempSum < n:
                    if len(primes[j:]) > length:
                        length = len(primes[j:])
                        sumPrimes.append(tempSum)
                else:
                    print(max(sumPrimes), length)
                    quit()
    i += 1