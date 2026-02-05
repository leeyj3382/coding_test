# 사용자 입력
n = int(input())

# n * n 테이블 : dp테이블
graph = []
# 입력 받으면서 초기화
for i in range(n):
	graph.append(list(map(int, input().split())))
	
# 플로이드 워셜 알고리즘
# 원래는 최소로 넣는데, 여긴 1/0으로 표시만 하면 되니까,
for k in range(n):
    for a in range(n):
        for b in range(n):
            # 이미 해당 노드가 1이면 방문 가능하니까, 패스
            if graph[a][b] == 1:
                continue
            # 그렇지 않으면, 경유 노선이 있다면 해당 노드를 1로 기록
            elif graph[a][b] == 0 :
                if graph[a][k] == 1 and graph[k][b] == 1:
                    graph[a][b] = 1

for i in range(n):
    print(" ".join(map(str, graph[i])))