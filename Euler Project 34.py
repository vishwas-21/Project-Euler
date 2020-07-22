import math
import collections


def getFactorialSum(n):
    facSum = 0
    temp = str(n)
    for num in temp:
        facSum += math.factorial(int(num))
    return facSum

answer = collections.deque([])
# Why 2540160! Because 9! * x <= 999----x times gives x as 7 and 9! * x = 2540160
for i in range(10, 2540160):
    if getFactorialSum(i) == i:
        answer.append(i)
    print(i)
print(answer)
print(sum((answer)))