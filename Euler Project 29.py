import math
import collections

arr = collections.deque([])
for i in range(2, 101):
    for j in range(2, 101):
        temp = math.pow(i, j)
        if temp not in arr:
            arr.append(temp)

print(len(arr))

