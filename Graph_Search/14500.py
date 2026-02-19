import sys

n, m = map(int, sys.stdin.readline().split())

board = []
for i in range(n):
    board.append(list(map(int, sys.stdin.readline().split())))
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [[False] * m for _ in range(n)]

def dfs(start, depth, total):
    global ans
    x, y = start
    if depth == 4:

        ans = max(ans, total)
        return
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
           continue
        if visited[nx][ny]:
            continue
        visited[nx][ny] = True
        dfs((nx,ny), depth+1, total + board[nx][ny])
        visited[nx][ny] = False

def exception(start):
    x, y = start
    pos = []

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
           continue
        pos.append(board[nx][ny])
    if len(pos) < 3:
        return 0
    elif len(pos) == 3:
        return sum(pos) + board[x][y]
    else:
        return sum(pos) - min(pos) + board[x][y]

ans = 0
for i in range(n):
    for j in range(m):
        visited[i][j] = True
        dfs((i,j), 1, board[i][j])
        visited[i][j] = False
        
        ans = max(ans, exception((i, j)))
        
print(ans)