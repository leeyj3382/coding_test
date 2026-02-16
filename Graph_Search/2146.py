import sys
from collections import deque

n = int(sys.stdin.readline().strip())

graph = []
for i in range(n):
    tmp = list(map(int, sys.stdin.readline().split()))
    graph.append(tmp)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
# 섬 번호 마킹 bfs
def bfs(start, mark):
    x, y = start
    q = deque()
    
    q.append((x, y))
    graph[x][y] = mark
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = mark
                q.append((nx, ny))

# 섬 번호 마킹 2부터 시작
mark = 2
for i in range(n):
    for j in range(n):
        # 이미 방문한 섬이라면 패스
        if graph[i][j] != 1:
            continue
        else:
            bfs((i,j), mark)
            mark += 1
# 최단 경로 찾는 bfs
def bfs_path(start, bone):
    x, y = start
    b = bone
    q = deque()
    # 최단 경로를 기록용 리스트
    dist = [[-1]*(n) for i in range(n)]
    q.append((x, y, b))
    dist[x][y] = 0
    while q:
        x, y, b = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if graph[nx][ny] != 0 and graph[nx][ny] != b:
                return dist[x][y]
            if graph[nx][ny] == 0 and dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx, ny, b))                
    return 10**18
    
result = 10**18
for i in range(n):
    for j in range(n):
        if graph[i][j] <= 1:
            continue
        for d in range(4):
            nx = i + dx[d]
            ny = j + dy[d]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if graph[nx][ny] != 0:
                continue
            tmp = bfs_path((i, j), graph[i][j])
            result = min(result, tmp)
            break
print(result)