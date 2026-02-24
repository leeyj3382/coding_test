import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
board = []
for i in range(n):
    tmp = list(map(int, sys.stdin.readline().split()))
    board.append(tmp)
psum = [[0] * (m+1) for i in range(n+1)]
# prefix sum table
for i in range(1, n+1):
    for j in range(1, m+1):
        psum[i][j] = psum[i-1][j] + psum[i][j-1] + board[i-1][j-1] - psum[i-1][j-1]
def wall(sr, sc, fr, fc):
    wall = psum[fr+1][fc+1] - psum[fr+1][sc] - psum[sr][fc+1] + psum[sr][sc]
    return wall
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
h, w, sr, sc, fr, fc = map(int, sys.stdin.readline().split())
sr -= 1
sc -= 1
fr -= 1
fc -= 1

INF = int(1e9)
dist = [[INF]*(m) for _ in range(n)]
def bfs(sr, sc, sr2, sc2, fr, fc):
    q = deque()
    dist[sr][sc] = 0
    q.append((sr,sc, sr2, sc2))
    cnt = 0
    if sr == fr and sc == fc:
        return 0
    while q:
        x, y , sr2, sc2= q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            nsr2 = sr2 + dx[i]
            nsc2 = sc2 + dy[i]
            if nsr2 < 0 or nsr2 >= n or nsc2< 0 or nsc2 >= m:
                continue
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if dist[nx][ny] != INF:
                continue
            if wall(nx, ny, nsr2, nsc2) != 0:
                continue
            q.append((nx, ny, nsr2, nsc2))
            cnt += 1
            dist[nx][ny] = dist[x][y] + 1
            if nx == fr and ny == fc:
                return dist[nx][ny]
            
    return -1
            
print(bfs(sr, sc, sr+h-1, sc+w-1, fr, fc))

        