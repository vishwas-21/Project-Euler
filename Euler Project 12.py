import math

def numDivisors(n):
    num = 0
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            if i == n // i:
                num += 1
            else:
                num += 2
    return num

def inTri(n):
    return n * (n + 1) // 2


i = 1
while True:
    if numDivisors(inTri(i)) >= 500:
        print("Amswer is", inTri(i))
        break
    print(i)
    i += 1