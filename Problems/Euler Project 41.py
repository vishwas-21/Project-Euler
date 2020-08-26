import math

def isPrime(n):
    if n > 0:
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True
    return False

num = ["7", "6", "5", "4", "3", "2", "1"]
maxNumber = 0
for i in num:
    num1 = num.copy()
    num1.remove(i)
    for j in num1:
        num2 = num1.copy()
        num2.remove(j)
        for k in num2:
            num3 = num2.copy()
            num3.remove(k)
            for l in num3:
                num4 = num3.copy()
                num4.remove(l)
                for m in num4:
                    num5 = num4.copy()
                    num5.remove(m)
                    for n in num5:
                        num6 = num5.copy()
                        num6.remove(n)
                        for o in num6:
                                integer = int(i+j+k+l+m+n+o)
                                if isPrime(integer):
                                    if integer > maxNumber:
                                        maxNumber = integer
                                        print(integer)

print("Max num is", maxNumber)

# This Problem is done by checking whether the number we need is in 1-9 digit number oe 1-8 or 1-7 so found it in 7 digit number