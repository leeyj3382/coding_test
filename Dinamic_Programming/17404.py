import sys
INF = int(1e9)
n = int(sys.stdin.readline())

costs = [[0] for _ in range(n)]
for i in range(n):
    costs[i] = list(map(int, sys.stdin.readline().split()))
ans = INF
# 첫 노드의 색 강제
for first in range(3):
    # dp 테이블을 dp[i][c] = 비용 즉, i번째 집을 c로 칠했을 때의 최저 누적 비용
    dp = [[INF]*3 for i in range(n)]
    dp[0][first] = costs[0][first]
    
    for i in range(1, n):
        dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + costs[i][0]
        dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + costs[i][1]
        dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + costs[i][2]
        
    for last in range(3):
        if last != first:
            ans = min(ans, dp[n-1][last])
            
print(ans)