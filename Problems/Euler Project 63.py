total = 0
for i in range(1, 10):
    j = 1
    while True:
        temp = str(pow(i, j))
        if len(temp) < j:
            break
        elif len(temp) == j:
            total += 1
        j += 1

print(total)
