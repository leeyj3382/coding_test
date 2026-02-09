import sys
import heapq
INF = int(1e9)
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

graph = [[] for i in range(n+1)]
for i in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b,c))
    
distance = [INF] * (n+1)
start, end = map(int, sys.stdin.readline().split())
def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        for nxt in graph[now]:
            cost = dist + nxt[1]
            if cost < distance[nxt[0]]:
                distance[nxt[0]] = cost
                heapq.heappush(q, (cost, nxt[0]))

dijkstra(start)

print(distance[end])