import sys

R, C, M = map(int, sys.stdin.readline().split())

board = [[None]*(C+1) for _ in range(R+1)]

dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, 1, -1]

def reverse_dir(d):
    if d == 1:
        return 2
    if d == 2:
        return 1
    if d == 3:
        return 4
    return 3

def move_shark(r, c, s, d):
    if d == 1 or d == 2:
        if R > 1:
            s %= (2 * (R - 1))
        else:
            s = 0
    else:
        if C > 1:
            s %= (2 * (C - 1))
        else:
            s = 0
    for _ in range(s):
        nx = r + dx[d]
        ny = c + dy[d]
        if nx < 1 or nx > R or ny < 1 or ny > C:
            d = reverse_dir(d)
            nx = r + dx[d]
            ny = c + dy[d]
        r, c = nx, ny
        
    return r, c, d

for _ in range(M):
    r, c, s, d, z = map(int, sys.stdin.readline().split())
    board[r][c] = [s, d, z]
result = 0

for fisher_col in range(1, C+1):
    for row in range(1, R+1):
        if board[row][fisher_col] is not None:
            result += board[row][fisher_col][2]
            board[row][fisher_col] = None
            break
    new_board = [[None]*(C+1) for _ in range(R+1)]
    for r in range(1, R+1):
        for c in range(1, C+1):
            if board[r][c] is None:
                continue
            s, d, z = board[r][c]
            nr, nc, nd = move_shark(r, c, s, d)
            
            if new_board[nr][nc] is None or new_board[nr][nc][2] < z:
                new_board[nr][nc] = (s, nd, z)
    board = new_board
    
print(result)
        