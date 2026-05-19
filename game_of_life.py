import copy
class Solution(object):
    def gameOfLife(self, board):
        n1 = len(board)
        n2 = len(board[0])
        org = copy.deepcopy(board)
        for i in range(n1):
            for j in range(n2):
                tl = org[i - 1][j - 1] if (i - 1 >= 0 and j - 1 >= 0) else 0
                l  = org[i][j - 1]     if (j - 1 >= 0) else 0
                dl = org[i + 1][j - 1] if (i + 1 < n1 and j - 1 >= 0) else 0
                t  = org[i - 1][j]     if (i - 1 >= 0) else 0
                tr = org[i - 1][j + 1] if (i - 1 >= 0 and j + 1 < n2) else 0
                r  = org[i][j + 1]     if (j + 1 < n2) else 0
                d  = org[i + 1][j]     if (i + 1 < n1) else 0
                dr = org[i + 1][j + 1] if (i + 1 < n1 and j + 1 < n2) else 0

                if (tl + l + dl + t + tr + r + d + dr) < 2:
                    board[i][j] = 0
                elif (tl + l + dl + t + tr + r + d + dr) > 3:
                    board[i][j] = 0
                elif (tl + l + dl + t + tr + r + d + dr) == 3:
                    board[i][j] = 1
                elif (tl + l + dl + t + tr + r + d + dr) == 3 or (tl + l + dl + t + tr + r + d + dr) == 2:
                    board[i][j] = org[i][j]
