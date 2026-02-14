import sys
# topology search
from collections import deque

n, m = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n+1)]
# 진입 차수를 기록
indegree = [0] * (n+1)

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    # a가 b보다 선행되어야 한다
    graph[a].append(b)
    # a는 b의 선행. 즉, 진입차수가 됨 => 진입차수 증가
    indegree[b] += 1
result = []
def topology_search():
    q = deque()
    # 진입 차수가 0인 애들을 전부 큐에 넣음
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)
            result.append(i)
    while q:
        now = q.popleft()
        for nxt in graph[now]:
            indegree[nxt] -= 1
            
            if indegree[nxt] == 0:
                q.append(nxt)
                result.append(nxt)
topology_search()
print(*result)