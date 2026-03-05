# 가중치 있는 그래프 + 양방향 간선(방향 없음)
# 기준점은 항상 1번 마을에 있는 음식점
# 다익스트라
import heapq

def solution(N, road, K):
    
    # 간선 정보를 입력(양방향)
    graph = [[] for i in range(N+1)]
    for i in range(len(road)):
        a, b, c = road[i]
        graph[a].append((b,c))
        graph[b].append((a,c))
        
    INF = int(1e9)
    distance = [INF] * (N+1)
    
    def dijkstra(start):
        q = []
        heapq.heappush(q, (0, start))
        distance[start] = 0
        
        while q:
            dist, now = heapq.heappop(q)
            if distance[now] < dist:
                continue
                
            for nxt in graph[now]:
                cost = dist + nxt[1]
                if cost < distance[nxt[0]]:
                    distance[nxt[0]] = cost
                    heapq.heappush(q, (cost, nxt[0]))
                    
    dijkstra(1)
    ans = 0
    for i in range(1, N+1):
        if distance[i] <= K:
            ans += 1
    return ans
        
        