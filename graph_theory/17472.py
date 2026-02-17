import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

graph = []
for i in range(n):
    tmp = list(map(int, sys.stdin.readline().split()))
    graph.append(tmp)
    
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# bfs_라벨링, 외곽 지역 리턴
def label(x, y, mark):
    q = deque()
    q.append((x, y))
    graph[x][y] = mark
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = mark
                q.append((nx, ny))

mark = 2
# label 호출해서 라벨링
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            label(i, j, mark)
            mark += 1
            
num_islands = mark - 2
if num_islands <= 1:
    print(0)
    sys.exit()

# 간선 만들기
INF = int(1e9)
best = [[INF] * (mark) for _ in range(mark)]

for x in range(n):
    for y in range(m):
        if graph[x][y] >= 2:
            a = graph[x][y]
            for k in range(4):
                nx, ny = x, y
                length = 0
                while True:
                    nx += dx[k]
                    ny += dy[k]
                    if not (0 <= nx < n and 0 <= ny < m):
                        break
                    if graph[nx][ny] == 0:
                        length += 1
                        continue
                    
                    # 다른 섬 도착
                    b = graph[nx][ny]
                    if b != a and length >= 2:
                        if length < best[a][b]:
                            best[a][b] = best[b][a] = length
                    break

edges = []
for a in range(2, mark):
    for b in range(a + 1, mark):
        if best[a][b] != INF:
            edges.append((best[a][b], a, b))
            
# 크루스칼
parent = [i for i in range(mark)]

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

        
edges.sort()
total = 0
cnt = 0

for cost, a, b in edges:
    if find(a) != find(b):
        union(a,b)
        total += cost
        cnt += 1
        if cnt == num_islands - 1:
            break
print(total if cnt == num_islands - 1 else -1)