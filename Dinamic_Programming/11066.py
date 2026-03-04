import sys

t = int(sys.stdin.readline().strip())
INF = int(1e9)

for _ in range(t):
    n = int(sys.stdin.readline().strip())
    a = list(map(int, sys.stdin.readline().split()))
    
    ps = [0] * (n+1)
    for i in range(n):
        ps[i+1] = ps[i] + a[i]
        
    def range_sum(i, j):
        return ps[j+1] - ps[i]
    dp = [[0]*n for _ in range(n)]
    
    for length in range(2, n+1):
        for i in range(0, n-length+1):
            j = i + length - 1
            best = INF
            s = range_sum(i, j)
            for k in range(i, j):
                cost = dp[i][k] + dp[k+1][j] + s
                if cost < best:
                    best = cost
                dp[i][j] = best
    print(dp[0][n-1])