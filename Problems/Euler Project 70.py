from tqdm import tqdm

def is_permutation(a, b):
    a, b = str(a), str(b)
    if len(a) != len(b):
        return False
    a, b = sorted(a), sorted(b)
    for i in range(len(a)):
        if a[i] != b[i]:
            return False
    return True


N = 10**7
is_prime = [True] * N
is_prime[0] = is_prime[1] = False
totient = [i for i in range(N)]

for i in tqdm(range(2, N)):
    if not is_prime[i]:
        continue
    for j in range(i, N, i):
        is_prime[j] = False
        totient[j] -= totient[j] // i

ans = [0, float('inf')]
for i in tqdm(range(2, N)):
    if is_permutation(i, totient[i]):
        if i / totient[i] < ans[1]:
            ans = [i, i / totient[i]]

print(f"Answer: {ans[0]}")