import sys
from collections import deque

input = sys.stdin.readline

n = int(input().strip())
board = [list(map(int, input().split())) for _ in range(n)]

# 상어 시작 위치 찾기
sx = sy = -1
for i in range(n):
    for j in range(n):
        if board[i][j] == 9:
            sx, sy = i, j
            board[i][j] = 0
            break
    if sx != -1:
        break
        
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

def bfs_find_prey(x, y, size):
    dist = [[-1] * n for _ in range(n)]
    q = deque()
    q.append((x, y))
    dist[x][y] = 0
    
    candidates = []
    best_d = None
    
    while q:
        cx, cy = q.popleft()
        d = dist[cx][cy]
        
        if best_d is not None and d > best_d:
            break
        
        for k in range(4):
            nx = cx + dx[k]
            ny = cy + dy[k]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if dist[nx][ny] != -1:
                continue
        
            if board[nx][ny] <= size:
                dist[nx][ny] = d +1
                q.append((nx, ny))
            
                if 0 < board[nx][ny] < size:
                    if best_d is None:
                        best_d = d + 1
                    candidates.append((nx, ny, d + 1))
    if not candidates:
        return None
    
    candidates.sort(key = lambda t : (t[2], t[0], t[1]))
    px, py, pd = candidates[0]
    return px, py, pd

size = 2
eaten = 0
time = 0

x, y = sx, sy

while True:
    res = bfs_find_prey(x, y, size)
    if res is None:
        break
    
    px, py, dist = res
    time += dist
    x, y = px, py
    
    board[x][y] = 0
    eaten += 1
    if eaten == size:
        size += 1
        eaten = 0
        
print(time)