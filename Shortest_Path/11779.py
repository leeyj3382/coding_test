import sys
import heapq

INF = int(1e9)

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    # 가중치 있는 단방향 간선
    graph[a].append((b,c))
# 최소 거리 테이블  
distance = [INF] * (n+1)
# 방문 노드 테이블 : 직전에 방문한 노드만 저장
prev = [0] * (n+1)

start, end = map(int, sys.stdin.readline().split())

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
                prev[i[0]] = now
                heapq.heappush(q, (cost, i[0]))

                
dijkstra(start)
path = []
cur = end
while cur != 0:
    path.append(cur)
    if cur == start:
        break
    cur = prev[cur]

path.reverse()

print(distance[end])
print(len(path))
print(" ".join(map(str, path)))