lines = [[1, 2, 3],
         [4, 3, 5],
         [6, 5, 7],
         [8, 7, 9],
         [10, 9, 2]]

def is_valid(arr):
    inner_indices = [2, 3, 5, 7, 9]
    for i in inner_indices:
        if arr[i - 1] == 10:
            return False
    return True

def is_magic(arr):
    req_s = sum(arr[i - 1] for i in lines[0])
    for el in lines:
        if sum([arr[i - 1] for i in el]) != req_s:
            return False
    return True

from itertools import permutations
from tqdm import tqdm
final_ans = 0
bar = tqdm(total=3628800)

for el in permutations([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]):
    bar.update(1)
    if not is_valid(el):
        continue
    if not is_magic(el):
        continue
    arr = list(el)
    ind = [arr[line[0] - 1] for line in lines].index(min([arr[line[0] - 1] for line in lines]))
    ans = ""
    for _ in range(5):
        ans += "".join([str(arr[i - 1]) for i in lines[ind]])
        ind = (ind + 1) % 5
    final_ans = max(final_ans, int(ans))

print("\n")
print(f"Answer: {final_ans}")