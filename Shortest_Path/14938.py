import sys
import heapq
INF = int(1e9)
n, m, r = map(int, sys.stdin.readline().split())
item = [0]

tmp = list(map(int, sys.stdin.readline().split()))
for t in tmp:
    item.append(t)
    
graph = [[] for _ in range(n+1)]
for _ in range(r):
    a, b, c = map(int, sys.stdin.readline().split())
    # a <-> b cost c
    graph[a].append((b, c))
    graph[b].append((a, c))


def dijkstra(start, m):
    # 시작점은 거리 0
    distance[start] = 0
    q = []
    heapq.heappush(q, (0, start))
    
    while q:
        dist, now = heapq.heappop(q)
        # 이미 방문 했으면 패스
        if dist > distance[now]:
            continue
        for nxt in graph[now]:
            cost = dist + nxt[1]
            # 수색 범위 넘어가면 패스
            if cost > m:
                continue
            if distance[nxt[0]] > cost:
                distance[nxt[0]] = cost
                heapq.heappush(q,(cost, nxt[0]))
max_item = 0
for i in range(1, n+1):
    # 최소 거리를 저장할 리스트    
    distance = [INF] * (n+1)
    dijkstra(i, m)
    tmp = 0
    for j in range(1, n+1):
        if distance[j] <= m:
            tmp += item[j]
    if max_item < tmp:
        max_item = tmp
print(max_item)