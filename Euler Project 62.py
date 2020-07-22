import time

start = time.time()
def get_digits(n):
    ar = [int(el) for el in str(n)]
    ar.sort()
    return ar


perDigits = []
perCount = []
perNums = []

i = 2
while 5 not in perCount:
    temp = pow(i, 3)
    arr = get_digits(temp)
    if arr in perDigits:
        ind = perDigits.index(arr)
        perCount[ind] += 1
        perNums[ind].append(i)
    else:
        perDigits.append(arr)
        perCount.append(1)
        perNums.append([i])
    i += 1
print("Answer is", min(perNums[ind]) ** 3)
print(time.time() - start)