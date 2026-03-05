import sys

n = int(sys.stdin.readline().strip())
t = [0] * (n)
p = [0] * (n)

for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    t[i] = a
    p[i] = b
# i일 까지의 최대 이익
dp = [0] * (n+1)

for i in range(n):
    # 이번 진료를 보지 않을 경우/불가한 경우
    dp[i+1] = max(dp[i+1], dp[i])
    
    ni = i + t[i]
    if ni <= n:
        dp[ni] = max(dp[ni], dp[i] + p[i])
    
print(dp[n])