import sys
from itertools import permutations
from collections import deque

n = int(sys.stdin.readline().strip())
scv = list(map(int, sys.stdin.readline().split()))
while len(scv) < 3:
    scv.append(0)

# 데미지를 줄 수 있는 경우의 수
dmg = list(set(permutations((9,3,1), 3)))
# 방문/거리 배열
dist = [[[-1]*61 for _ in range(61)] for __ in range(61)]

def bfs(a, b, c):
    q = deque()
    q.append((a,b,c))
    dist[a][b][c] = 0
    
    while q:
        a, b, c = q.popleft()
        if a == 0 and b == 0 and c == 0:
            print(dist[0][0][0])
            return
        cur = dist[a][b][c]
        for case in dmg:
            x, y, z = case
            na = max(0, a - x)
            nb = max(0, b - y)
            nc = max(0, c - z)
            
            if dist[na][nb][nc] == -1:
                dist[na][nb][nc] = cur + 1
                q.append((na,nb,nc))
                
a = scv[0]
b = scv[1]
c = scv[2]

bfs(a, b, c)