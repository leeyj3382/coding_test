from collections import deque

def bfs(starts) :
	q = deque()
	days = 0
	for start in starts:
		q.append(start)
	while q:
		v = q.popleft()
		x = v[0]
		y = v[1]
		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]
			
			if(nx < 0 or nx >= n or ny < 0 or ny >= m):
				continue
			if(graph[nx][ny] == 1 or graph[nx][ny] == -1):
				continue
			if(graph[nx][ny] == 0):
				q.append((nx,ny))
				graph[nx][ny] = graph[x][y] + 1

m, n = map(int, input().split())

graph = []
for i in range(n):
	graph.append(list(map(int, input().split())))
	
has_zero = False
for row in graph:
	if 0 in row:
		has_zero = True
		break
if not has_zero:
	print(0)
	exit()
	
starts = []
for i in range(n):
	for j in range(m):
		if graph[i][j] == 1:
			starts.append((i, j))
			
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

bfs(starts)

max_day = 1
for row in graph:
	if 0 in row:
		print(-1)
		break
	max_day = max(max_day, max(row))
else:
	print(max_day-1)