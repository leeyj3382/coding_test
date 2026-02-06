import heapq
import sys
# 도달 불가능
INF = int(1e9)

n, e = map(int, sys.stdin.readline().split())
# 거리 테이블 초기화
distance = [INF] * (n+1)
# 그래프 초기화
graph = [[] for _ in range(n+1)]
# 간선 정보 입력 : 가중치가 있는 양방향 간선
for _ in range(e):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

# 경유 노드
v1, v2 = map(int, sys.stdin.readline().split())

def dijkstra(start):
    distance = [INF] * (n+1)
    q = []
    heapq.heappush(q,(0, start))
    distance[start] = 0
    
    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    return distance            


d1 = dijkstra(1)
dv1 = dijkstra(v1)
dv2 = dijkstra(v2)

short1 = d1[v1] + dv1[v2] + dv2[n]
short2 = d1[v2] + dv2[v1] + dv1[n]
result = min(short1, short2)

print(result if result < INF else -1)