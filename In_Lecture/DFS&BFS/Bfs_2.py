from collections import deque

def bfs(x,y):
	queue = deque()
	queue.append((x,y))

	while queue:
		x, y = queue.popleft()
		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]
			# 미로 찾기 공간을 벗어난 경우 무시
			if nx < 0 or nx >= n or ny < 0 or ny >= m:
				continue
			# 벽인 경우 무시
			if graph[nx][ny] == 0:
				continue
			
			if graph[nx][ny] == 1:
				graph[nx][ny] = graph[x][y] + 1
				queue.append((nx,ny))
				
	return graph[n-1][m-1]


dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


n, m = map(int, input().split())
graph = []
for i in range(n):
	graph.append(list(map(int, input())))
	
print(bfs(0,0))