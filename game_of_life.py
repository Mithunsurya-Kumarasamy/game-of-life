import copy
import random

n1 = random.randint(3, 6)
n2 = random.randint(3, 6)
board = [[random.choice([0, 1]) for _ in range(n2)] for _ in range(n1)]

print("--- Initial Board State ---")
for row in board:
    print(row)
print("-" * 27)

original = copy.deepcopy(board)

for i in range(n1):
    for j in range(n2):
        tl = original[i - 1][j - 1] if (i - 1 >= 0 and j - 1 >= 0) else 0
        l  = original[i][j - 1]     if (j - 1 >= 0) else 0
        dl = original[i + 1][j - 1] if (i + 1 < n1 and j - 1 >= 0) else 0
        t  = original[i - 1][j]     if (i - 1 >= 0) else 0
        tr = original[i - 1][j + 1] if (i - 1 >= 0 and j + 1 < n2) else 0
        r  = original[i][j + 1]     if (j + 1 < n2) else 0
        d  = original[i + 1][j]     if (i + 1 < n1) else 0
        dr = original[i + 1][j + 1] if (i + 1 < n1 and j + 1 < n2) else 0

        total_neighbors = tl + l + dl + t + tr + r + d + dr

        if total_neighbors < 2:
            board[i][j] = 0
        elif total_neighbors > 3:
            board[i][j] = 0
        elif total_neighbors == 3:
            board[i][j] = 1
        elif total_neighbors == 2:
            board[i][j] = original[i][j] 

print("\n--- Output Board State ---")
for row in board:
    print(row)
print("-" * 26)