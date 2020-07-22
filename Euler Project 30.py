import math
import collections


def isSumOfFifthPowerDigits(n):
    sumOfNum = 0
    temp = n
    while n != 0:
        sumOfNum += math.pow((n % 10), 5)
        n = n // 10
    return int(sumOfNum) == temp


arr = collections.deque([])

for i in range(2, 236197):
    if isSumOfFifthPowerDigits(i):
        arr.append(i)

print(sum(arr))


