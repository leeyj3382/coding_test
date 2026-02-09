import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
# 그래프 입력 받고
graph = []
for i in range(n):
    tmp = list(map(int, sys.stdin.readline().strip()))
    graph.append(tmp)

# 3차원 리스트
# dist [b][a][b] : (a, b)에 도착했을 때 최단거리
# b = 0 : 벽을 아직 부수지 않음 , b = 1: 벽을 이미 부숨
dist = []
for i in range(2):
    dist.append([[0]*(m) for _ in range (n)])
    
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    q = deque()
    # 처음 위치 고정 + 길이며, 아직 부수지 않은 상태
    q.append((0, 0, 0))
    dist[0][0][0] = 1
    
    while q:
        b, x, y = q.popleft()
        if x == n-1 and y == m-1:
            return dist[b][x][y]
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 다음 칸이 길이고, 아직 방문 안 했으면
            if graph[nx][ny]==0 and dist[b][nx][ny]==0:
                dist[b][nx][ny] = dist[b][x][y] + 1
                q.append((b,nx,ny))
            
            # 다음 칸이 벽인데, 벽을 부술 수 있고(b = 0), 방문한 노드가 아니라면
            elif graph[nx][ny] == 1 and b == 0 and dist[1][nx][ny] == 0:
                dist[1][nx][ny] = dist[b][x][y]+1
                q.append((1, nx, ny))
                
    return -1

print(bfs())