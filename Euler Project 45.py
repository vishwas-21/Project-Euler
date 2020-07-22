import math

def isPentaNum(x):
    sol = (math.sqrt(1 + 24 * x) + 1) / 6
    if int(sol) == sol:
        return True
    return False

def isHexaNum(x):
    sol = (math.sqrt(1 + 8 * x) + 1) / 4
    if int(sol) == sol:
        return True
    return False

i = 0
num = 285
nums = []
while i < 2:
    temp = num * (num + 1) // 2
    if isHexaNum(temp) and isPentaNum(temp):
        i += 1
        nums.append(num)
    num += 1
    print(num)

print(nums)
