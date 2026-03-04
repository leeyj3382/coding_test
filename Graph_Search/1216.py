import sys
from collections import deque

m, n = map(int, sys.stdin.readline().split())

board = []
for i in range(n):
    tmp = list(map(int, sys.stdin.readline().strip()))
    board.append(tmp)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
    
INF = int(1e9)
dist = [[INF] * (m) for _ in range(n)]
def bfs(start):
    q = deque()
    x, y = start
    q.append((x, y))
    dist[x][y] = 0
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 이미 방문한 경우
            if dist[nx][ny] != INF:
                continue
            dist[nx][ny] = dist[x][y] + board[nx][ny]
            if board[nx][ny] == 0:
                q.appendleft((nx, ny))
            else:
                q.append((nx, ny))

bfs((0,0))
print(dist[n-1][m-1])