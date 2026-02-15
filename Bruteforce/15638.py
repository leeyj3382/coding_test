import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = []
cctv = []

for i in range(n):
    row = list(map(int, input().split()))
    board.append(row)
    for j in range(m):
        if row[j] in [1,2,3,4]:
            cctv.append((row[j], i, j))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


dirs = {
    1: [[0], [1], [2], [3]],
    2: [[0, 2], [1, 3]],
    3: [[0, 1], [1, 2], [2, 3], [3, 0]],
    4: [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
    5: [[0, 1, 2, 3]],
}

def watch(x, y, dlist):
    changed = []
    for d in dlist:
        nx, ny = x, y
        while True:
            nx += dx[d]
            ny += dy[d]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                break
            if board[nx][ny] == 6:
                break
            if board[nx][ny] == 0:
                board[nx][ny] = -1
                changed.append((nx, ny))
    return changed

ans = int(1e9)

def dfs(idx):
    global ans
    if idx == len(cctv):
        blind = sum(board[i][j] == 0 for i in range(n) for j in range(m))
        ans = min(ans, blind)
        return
    
    t, x, y = cctv[idx]
    for dlist in dirs[t]:
        changed = watch(x, y, dlist)
        dfs(idx+1)
        for cx, cy in changed:
            board[cx][cy] = 0
dfs(0)
print(ans)