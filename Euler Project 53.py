import math

def combination(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

ways = 0
for n in range(1,  101):
    for j in range(0, n // 2):
        if combination(n, j) >= 1000000:
            if n % 2 == 0:
                temp = n // 2 - j
                ways += 2 * temp + 1
                break
            else:
                temp = n // 2 - j + 1
                ways += 2 * temp
                break

    print(n)


print("Answer is", ways)