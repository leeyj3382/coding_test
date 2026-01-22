from collections import deque


def bfs(start, graph, distance) :
	
	q = deque([start])
	# 시작 노드의 값은 1이고
	distance[start] = 1
	
	while q:
		v = q.popleft()
		
		for i in graph[v] :
			if distance[i] == -1:
				q.append(i)
				distance[i] = distance[v] + 1


n, m = map(int, input().split())

graph = [ [] for _ in range(n+1) ]

for i in range(m) :
	a, b = map(int, input().split())
	
	graph[a].append(b)
	graph[b].append(a)

for i in range(n+1) :
	graph[i].sort()
	

result = []
for i in range(1, n+1) :
	distance = [-1] * (n+1)
	bfs(i, graph, distance)
	result.append(sum(distance))


print( result.index(min(result)) + 1 )
