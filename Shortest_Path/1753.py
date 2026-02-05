import sys
import heapq

INF = int(1e9)
# 노드 개수, 간선 개수
n, m = map(int, sys.stdin.readline().split())
# 시작 노드
start = int(sys.stdin.readline())
# graph
graph = [[] for _ in range(n+1)]
# distance
distance = [INF] * (n+1)
# 이동 경로 업데이트
for i in range(m):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append((v,w))
    
def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
                
                
dijkstra(start)

for i in range(1, n+1):
    if distance[i] != INF:
        print(distance[i])
    else:
        print("INF")