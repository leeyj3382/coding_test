import sys

n = int(sys.stdin.readline())

# 각 집에 칠하는 색상별 가격
costs = []
for i in range(n):
    tmp = list(map(int, sys.stdin.readline().split()))
    costs.append(tmp)
# dp[i][color] = sum cost  
# i번째 집을 color로 칠했을 때, 누적 합
# 근데, 불가능한 선택지를 표시하려면, INF로 초기화
INF = int(1e9)
dp = [[INF]*3 for i in range(n)]

# 3색 동안
for first in range(3):
    # 첫 집의 색을 먼저 선정
    dp[0][first] = costs[0][first]
    # 남은 노드에 대해 순회
    for i in range(1, n):
        # 지금 0번을 칠한다면 => 앞이 1일때와 2일떄 중 최소 + 0번 비용
        dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + costs[i][0]
        # 지금 1번을 칠한다면 => 앞이 0일때와 2일떄 중 최소 + 1번 비용
        dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + costs[i][1]
        # 지금 2번을 칠한다면 => 앞이 0일때와 1일떄 중 최소 + 2번 비용
        dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + costs[i][2]
        
print(min(dp[n-1]))