import sys
sys.setrecursionlimit(10**7)
n, l, r = map(int, sys.stdin.readline().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, union):
    # 시작점 방문처리
    visited[x][y] = True
    union.append((x,y))
    # 상, 하, 좌, 우 확인
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= n or ny <0 or ny >= n:
            continue
        if not visited[nx][ny]:
            # 범위 안에 있다면,
            if l <= abs(graph[x][y] - graph[nx][ny]) <= r:
                dfs(nx, ny, union)
day = 0
while True:
    visited = [[False]*n for _ in range(n)]
    moved = False
    for i in range(n):
        for j in range(n):
            if visited[i][j] == True:
                continue
            # dfs 돌리고
            union = []
            dfs(i,j,union)
            
            if len(union) <= 1:
                continue
            
            moved = True
            # union 애들 평균 내서 분할
            total = 0
            for mem in union:
                x, y = mem
                total += graph[x][y]
            new = total // len(union)
            # 연합 애들 값 갱신
            for mem in union:
                x, y = mem
                graph[x][y] = new
    if not moved:
        print(day)
        break
    day += 1