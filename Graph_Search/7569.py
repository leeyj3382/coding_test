import sys
from collections import deque

m, n, h = map(int, sys.stdin.readline().split())
# 3차원 리스트
graph = []
for _ in range(h):
    # 2차원 리스트
    tmp = []
    for i in range(n):
        tmp.append(list(map(int, sys.stdin.readline().split())))
    # 를 append 해서 3차원으로
    graph.append(tmp)

# 이미 익어있는 애들만 있으면 조기종료
flag = -1
for z in range(h):
    for x in range(n):
        for y in range(m):
            if graph[z][x][y]== 0:
                flag = 0
                break
        if flag == 0:
            break
    if flag == 0:
        break
if flag == -1:
    print(0)
    exit()
        
        
# 6방향 벡터 정의
dz = [-1, 1, 0, 0, 0, 0]
dx = [0, 0, -1, 1, 0, 0]
dy = [0, 0, 0, 0, -1, 1]
def bfs(starts):
    q = deque()
    # 익어 있는 애들(값이 1인 애들)을 일단 받고 -> 큐에 다 넣음
    for start in starts:
        q.append(start)
    
    while q:
        z, x, y = q.popleft()
        # 6방향에 대해 검사
        for i in range(6):
            nz = z + dz[i]
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위 벗어나면 패스
            if nz < 0 or nz >= h or nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 0이 아니면(이미 익었거나, 벽이거나) 패스
            if graph[nz][nx][ny] != 0:
                continue
            # 익지 않은 토마토면, 언제 익게 되었는지를 기록(이전 노드 + 1)
            graph[nz][nx][ny] = graph[z][x][y] + 1
            q.append((nz,nx,ny))
            
# 이미 익어있는 애들 검사 => 시작점
starts =[]
for z in range(h):
    for x in range(n):
        for y in range(m):
            if graph[z][x][y]== 1:
                starts.append((z,x,y))
# 호출
bfs(starts)

# 익지 않은 애가 있는지(0이 아직 남아있는지) 확인 => 있으면 -1 출력하고 조기종료
flag_zero = -1
for z in range(h):
    for x in range(n):
        for y in range(m):
            if graph[z][x][y]== 0:
                flag_zero = 0
                break
        if flag_zero == 0:
            break
    if flag_zero == 0:
        break
if flag_zero == 0:
    print(-1)
    exit()
    
max_result = 0
for z in range(h):
    for x in range(n):
        for y in range(m):
            if graph[z][x][y] > max_result:
                max_result = graph[z][x][y]

print(max_result-1)