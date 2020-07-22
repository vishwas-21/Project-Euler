import time


start = time.time()
def get_tria(tria):
    i = 44
    temp = i * (i + 1) // 2
    while temp < 10000:
        if temp >= 1000:
            tria.append(temp)
        i += 1
        temp = i * (i + 1) // 2

def get_squa(squa):
    i = 30
    temp = i * i
    while temp < 10000:
        if temp >= 1000:
            squa[int(str(temp)[:2])].append(temp)
        i += 1
        temp = i * i

def get_penta(penta):
    i = 25
    temp = i * (3 * i - 1) // 2
    while temp < 10000:
        if temp >= 1000:
            penta[int(str(temp)[:2])].append(temp)
        i += 1
        temp = i * (3 * i - 1) // 2

def get_hexa(hexa):
    i = 22
    temp = i * (2 * i - 1)
    while temp < 10000:
        if temp >= 1000:
            hexa[int(str(temp)[:2])].append(temp)
        i += 1
        temp = i * (2 * i - 1)

def get_hetpa(hepta):
    i = 20
    temp = i * (5 * i - 3) // 2
    while temp < 10000:
        if temp >= 1000:
            hepta[int(str(temp)[:2])].append(temp)
        i += 1
        temp = i * (5 * i - 3) // 2

def get_octa(octa):
    i = 18
    temp = i * (3 * i - 2)
    while temp < 10000:
        if temp >= 1000:
            octa[int(str(temp)[:2])].append(temp)
        i += 1
        temp = i * (3 * i - 2)

tria = []
squa = [[]for _ in range(100)]
penta = [[]for _ in range(100)]
hexa = [[]for _ in range(100)]
hepta = [[]for _ in range(100)]
octa = [[]for _ in range(100)]                      # Solved using Backtracking
get_tria(tria)
get_squa(squa)
get_penta(penta)
get_hexa(hexa)
get_hetpa(hepta)
get_octa(octa)

def check(n1, n2):
    return str(n1)[-2:] == str(n2)[:2]
def solve_it(num, arr, num_arr):
    if len(num_arr) == 6:
        if check(num_arr[-1], num_arr[0]):
            print("Answer is ", sum(num_arr), "which is sum of", *num_arr)
            print(time.time() - start)
            quit()
        else:
            return
    el = int(str(num)[-2:])
    if 's' not in arr:
        temp = squa[el]
        for e in temp:
            solve_it(e, arr + ['s'], num_arr + [e])
    if 'p' not in arr:
        temp = penta[el]
        for e in temp:
            solve_it(e, arr + ['p'], num_arr + [e])
    if 'x' not in arr:
        temp = hexa[el]
        for e in temp:
            solve_it(e, arr + ['x'], num_arr + [e])
    if 'h' not in arr:
        temp = hepta[el]
        for e in temp:
            solve_it(e, arr + ['h'], num_arr + [e])
    if 'o' not in arr:
        temp = octa[el]
        for e in temp:
            solve_it(e, arr + ['o'], num_arr + [e])

for i in tria:
    solve_it(i, ['t'], [i])
