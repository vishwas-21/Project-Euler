def con_of_e(n):
    arr = [2, 1, 2]
    k = 2
    while len(arr) < n:
        arr.extend([1, 1, 2 * k])
        k += 1
    num = 1
    den = 0
    for i in range(n - 1, -1, -1):
        num, den = den, num
        num += (den * arr[i])
    return (num, den)

ans = con_of_e(100)
print(sum(int(i) for i in str(ans[0])))