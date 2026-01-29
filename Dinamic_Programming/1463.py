n = int(input())

# n까지 기록할 수 있는 dp 테이블 : 초기값 INF
dp = [10001 for i in range(n+1)]
dp[0] = 0
dp[1] = 0
for i in range(2, n+1):
    # 1 빼기
    dp[i] = min(dp[i], dp[i-1] + 1)
    # 3 나누기가 가능하면 => 체크
    if i%3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1)
    # 2 나누기가 가능하면 => 체크
    if i%2 == 0:
        dp[i] = min(dp[i], dp[i//2] + 1)

        
print(dp[n])