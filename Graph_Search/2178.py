from collections import deque


def bfs(start, graph):
	q = deque()
	q.append(start)
	
	while q:
		v = q.popleft()
		x = v[0]
		y = v[1]
		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]
			if( nx >= n or nx < 0 or ny>= m or ny < 0) :
				continue
			if ( graph[nx][ny] == 0):
				continue
			if ( graph[nx][ny] ==1 ):
				q.append((nx, ny))
				graph[nx][ny] = graph[x][y] + 1


n, m = map(int, input().split())

graph = []

for i in range(n):
	graph.append(list(map(int, input())))
	
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

	
bfs((0,0), graph)
print(graph[n-1][m-1])