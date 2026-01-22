from collections import deque

def dfs(v, graph, visited) :
	# 시작 노드 방문처리
	visited[v] = True
	print(v, end = ' ')
	
	# 시작 노드의 방문하지 않은 인접한 노드에 대해서
	# 재귀 호출을 통해 dfs 실행
	for i in graph[v] :
		if not visited[i] :
			dfs(i, graph, visited)

def bfs(v, graph, visited) :
	# 큐 객체 생성 및 시작 노드 삽입
	q = deque([v])
	visited[v] = True
	
	while q:
		# 최상단 노드 꺼내고
		v = q.popleft()
		print(v, end = ' ')
		
		# 꺼낸 노드의 방문하지 않은 인접한 노드 추가
		for i in graph[v] :
			if not visited[i] :
				q.append(i)
				visited[i] = True
	

n, m, v = map(int, input().split())

# graph 초기화(빈 리스트를 n+1개 생성) ; 0번쨰는 사용하지 않음
graph = [[] for _ in range(0,n+1)]

# 이웃한 노드 기록
for i in range(m) :
	# 한 줄 읽고, 두 노드 매핑
	node_a, node_b = map(int, input().split())
		
	# 그게 아니라면
	graph[node_a].append(node_b)
	graph[node_b].append(node_a)
	
for i in range(1, n+1):
    graph[i].sort()

# 방문 여부 확인 초기화
visited = [False] * (n+1)
dfs(v, graph, visited)
print()
# 방문 여부 확인 초기화
visited = [False] * (n+1)
bfs(v, graph, visited)
print()