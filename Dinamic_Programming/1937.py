n = int(input())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
d = []
for _ in range(n):
    d.append(list(0 for i in range(n)))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    # 이미 계산한 칸이라면 리턴
    if d[x][y] != 0:
        return d[x][y]
    
    # 지금 칸 먹음
    d[x][y] = 1
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        # 만약 다음 칸이 더 크면
        if graph[x][y] < graph[nx][ny]:
            # 재귀 호출 해서, 깊이탐색 하고, 최대값을 dp테이블에 캐싱
            d[x][y] = max(d[x][y], 1 + dfs(nx, ny))
    return d[x][y]

result = 0
for i in range(n):
    for j in range(n):
        result = max(result, dfs(i,j))
        
print(result)
