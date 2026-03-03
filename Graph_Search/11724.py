import sys
from collections import deque
n, m = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(1+n)]
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n+1)
def bfs(start):
    visited[start] = True
    q = deque()
    q.append(start)
    
    while q:
        now = q.popleft()
        for nxt in graph[now]:
            if not visited[nxt]:
                visited[nxt] = True
                q.append(nxt)
count = 0

for i in range(1, n+1):
    if visited[i] == False:
        bfs(i)
        count += 1
        
print(count)