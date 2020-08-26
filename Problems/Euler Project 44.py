import math
import time


start = time.time()
def isPentaNum(x):
    sol = (math.sqrt(1 + 24 * x) + 1) / 6
    if int(sol) == sol:
        return True
    return False


def inPenta(x):
    return x * (3 * x - 1) // 2

check = 1
n1 = 1
while 1:
    n1 = 1
    while n1 < check:                                       #Here I checked Only till the term I choose because as I Used two conditions nothing is missed
        temp = inPenta(n1) + inPenta(check)
        if isPentaNum(temp):
            if isPentaNum(temp + inPenta(n1)):          #Here answer will inPenta of check as we know
                print(n1, inPenta(check))
                print(time.time() - start)
                quit()
        temp = inPenta(check) - inPenta(n1)
        if isPentaNum(temp):                                #Here n1 becomes checking term and check becomes sum term
            if isPentaNum(temp + inPenta(check)):
                print(inPenta(n1), check, temp)    #--> Here answer will be in penta of n1
                print(time.time() - start)
                quit()
        n1 += 1
        print(n1, check)
    check += 1
