from collections import deque
from itertools import combinations


def bfs(starts, simul_graph):
	q = deque()
	for start in starts:
		q.append(start)
	while q:
		x, y = q.popleft()
		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]
			
			if (nx < 0 or nx >= n or ny < 0 or ny >= m):
				continue
			if (simul_graph[nx][ny] == 1):
				continue
			
			if (simul_graph[nx][ny] == 0):
				q.append((nx, ny))
				simul_graph[nx][ny] = 2



n, m = map(int, input().split())

graph = []
for i in range(n):
	graph.append(list(map(int, input().split())))
	
starts = []
for i in range(n):
	for j in range(m):
		if graph[i][j] == 2:
			starts.append((i,j))
			
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
	
zero_loc = []
for i in range(n):
	for j in range(m):
		if graph[i][j] == 0:
			zero_loc.append((i,j))
			
wall_loc = combinations(zero_loc, 3)
	
max_survive = 0

for wall in wall_loc :
	wall_1_x, wall_1_y = wall[0][0], wall[0][1]
	wall_2_x, wall_2_y = wall[1][0], wall[1][1]
	wall_3_x, wall_3_y = wall[2][0], wall[2][1]
	
	simul_graph = [row[:] for row in graph]
	simul_graph[wall_1_x][wall_1_y] = 1
	simul_graph[wall_2_x][wall_2_y] = 1
	simul_graph[wall_3_x][wall_3_y] = 1
	
	bfs(starts, simul_graph)
	
	count = 0
	for i in range(n):
		for j in range(m):
			if simul_graph[i][j] == 0:
				count += 1
	if max_survive < count:
		max_survive = count
	
print(max_survive)
	
