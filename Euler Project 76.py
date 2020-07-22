
def count_summations(n):
    arr = [0 for i in range(n + 1)]
    arr[0] = 1                                  # This is Working based on calculating num of ways of counting i including j and without j
    for i in range(1, n):
        for j in range(i, n + 1):
            arr[j] += arr[j - i]
    return arr[n]

print(count_summations(100))