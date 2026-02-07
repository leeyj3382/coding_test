from collections import deque
import sys
INF = (1e9)


n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
indegree = [0] * (n+1)

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    indegree[b] += 1
# 각 과목이 언제 이수 가능한지  
each = [0]*(n+1)
def topology_sort():
    q = deque()
    result = []
    # 진입차수 0인 애들 큐에 넣기
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)
            each[i] = 1
    while q:
        now = q.popleft()
        result.append(now)
        # 뺀 녀석과 연결된(뺀 녀석이 가리키는) 노드들 진입차수 감소
        for i in graph[now]:
            indegree[i] -= 1
            each[i] = max(each[i], each[now]+1)
            # 진입차수가 0이 된 녀석이 있으면 큐에 다시 넣음
            if indegree[i] == 0:
                q.append(i)


topology_sort()

for i in range(1, n+1):
    print(each[i], end = ' ')