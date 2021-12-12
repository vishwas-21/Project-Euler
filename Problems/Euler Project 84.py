import random
from collections import deque
from tqdm import tqdm
DICE_FACES = 4
board = [
    "GO", "A1", "CC1", "A2", "T1", "R1", "B1", "CH1", "B2", "B3", "JAIL",
    "C1", "U1", "C2", "C3", "R2", "D1", "CC2", "D2", "D3", "FP",
    "E1", "CH2", "E2", "E3", "R3", "F1", "F2", "U2", "F3", "G2J",
    "G1", "G2", "CC3", "G3", "R4", "CH3", "H1", "T2", "H2"
]
ans = [0] * len(board)

def get_action():
    a = random.randint(1, DICE_FACES) 
    b = random.randint(1, DICE_FACES)
    return a + b, int(a == b)

def next_R(c):
    while board[c][0] != 'R':
        c += 1
        c %= len(board)
    return c

def next_U(c):
    while board[c][0] != 'U':
        c += 1
        c %= len(board)
    return c

def go_back3(c):
    return (len(board) + c - 3) % len(board)

def cycle_arr(arr):
    return arr[1:] + [arr[0]]

def str_(x):
    if x < 10:
        return "0" + str(x)
    return str(x)

def run_simulation(n):
    global ans
    current_position = 0
    ccs = [0, 10] + [-1] * 14
    chs = [0, 10, 11, 24, 39, 5, next_R, next_R, next_U, go_back3] + [-1] * 6

    dq = deque(maxlen=3)
    for i in tqdm(range(n)):
        action, e = get_action()
        current_position = (current_position + action) % len(board)
        dq.append(e)
        if sum(dq) == 3:
            current_position = 10
            dq.clear()
        
        if board[current_position][:2] == "CH":
            a = chs[0]
            if a != -1:
                if isinstance(a, int):
                    current_position = a
                else:
                    current_position = a(current_position)
            chs = cycle_arr(chs)
        if board[current_position][:2] == "CC":
            a = ccs[0]
            if a != -1:
                current_position = a
            ccs = cycle_arr(ccs)
        if board[current_position] == "G2J":
            current_position = 10
        
        ans[current_position] += 1
    
n_games = 10
n_steps = 1000000
print(f"Running {n_games} games with {n_steps} steps each")

for i in range(n_games):
    run_simulation(n_steps)

ans = [[i, ans[i] / sum(ans)] for i in range(len(ans))]
ans.sort(key=lambda x: x[1], reverse=True)
print("Answer: " + "".join([str_(x[0]) for x in ans[:3]]))
    


