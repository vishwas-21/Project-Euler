n = 1001
arr = [[0 for _ in range(n)] for _ in range(n)]
i = j = n // 2
k = 1
num = 2
arr[i][j] = 1
while i != 0 or j != n - 1:
    if i == 0:
        while j != n - 1:
            arr[i][j + 1] = num
            num += 1
            j += 1
        break
    # Right
    for l in range(k):
        arr[i][j + 1] = num
        num += 1
        j += 1
    #Down
    for l in range(k):
        arr[i + 1][j] = num
        num += 1
        i += 1
    k += 1
    #Left
    for l in range(k):
        arr[i][j - 1] = num
        num += 1
        j -= 1
    #Up
    for l in range(k):
        arr[i - 1][j] = num
        num += 1
        i -= 1
    k += 1

sumTotal = 0
for i in range(n):
    sumTotal += arr[i][i] + arr[i][n - i - 1]
print(sumTotal - 1)