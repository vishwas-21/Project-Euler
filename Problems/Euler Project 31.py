import time
start = time.time()
ways = 0
for i in [0, 1]:
    sum = i * 200
    if sum == 200:
        ways += 1
        print(ways, i)
        sum -= i * 200
        continue
    for j in [0, 1, 2]:
        sum += j * 100
        if sum > 200:
            sum -= j * 100
            break
        if sum == 200:
            ways += 1
            print(ways, i, j)
            sum -= j * 100
            continue
        for k in [0, 1, 2, 3, 4]:
            sum += k * 50
            if sum > 200:
                sum -= k * 50
                break
            if sum == 200:
                ways += 1
                print(ways, i, j, k)
                sum -= k * 50
                continue
            for l in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
                sum += l * 20
                if sum > 200:
                    sum -= l * 20
                    break
                if sum == 200:
                    ways += 1
                    print(ways, i, j, k, l)
                    sum -= l * 20
                    continue
                for m in [n for n in range(21)]:
                    sum += m * 10
                    if sum > 200:
                        sum -= m * 10
                        break
                    if sum == 200:
                        ways += 1
                        print(ways, i, j, k, l, m)
                        sum -= m * 10
                        continue
                    for n in [k for k in range(41)]:
                        sum += n * 5
                        if sum > 200:
                            sum -= n * 5
                            break
                        if sum == 200:
                            ways += 1
                            print(ways, i, j, k,  l, m, n)
                            sum -= n * 5
                            continue
                        for o in [num for num in range(101)]:
                            sum += o * 2
                            if sum > 200:
                                sum -= o * 2
                                break
                            if sum == 200:
                                ways += 1
                                print(ways, i, j, k, l, m, n, o)
                                sum -= o * 2
                                continue
                            for p in [num for num in range(201)]:
                                sum += p * 1
                                if sum > 200:
                                    sum -= p * 1
                                    break
                                if sum == 200:
                                    ways += 1
                                    print(ways, i, j, k, l, m, n, o, p)
                                    sum -= p * 1
                                    continue
                                sum -= p * 1
                            sum -= o * 2
                        sum -= n * 5
                    sum -= m * 10
                sum -= l * 20
            sum -= k * 50
        sum -= j * 100
    sum -= i * 200

print(ways)
print(time.time() - start)