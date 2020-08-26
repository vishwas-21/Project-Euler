import math


def isRightAngTri(a, b, c):
    if math.pow(a, 2) == math.pow(b, 2) + math.pow(c, 2) or math.pow(b, 2) == math.pow(a, 2) + math.pow(c, 2) or math.pow(c, 2) == math.pow(b, 2) + math.pow(a, 2):
        return True
    return False

def numPossibleTri(p):
    possible = []
    for a in range(1, p // 2):
        for b in range(1, p // 2):
            c = p - a - b
            if a + b > c and b + c > a and c + a > b :
                if isRightAngTri(a, b, c):
                    arr = [a, b, c]
                    arr.sort()
                    if arr not in possible:
                        possible.append(arr)
    return len(possible)


maxNumber = 0
p = 0
for i in range(1, 1000):
    temp = numPossibleTri(i)
    if temp > maxNumber:
        maxNumber = temp
        p = i
    print(i)
print("Max is", maxNumber, "for p =", p)