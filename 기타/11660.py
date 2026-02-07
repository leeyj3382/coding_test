import sys

n, m = map(int, sys.stdin.readline().split())
# 테이블
table = []
for i in range(n):
    table.append(list(map(int, sys.stdin.readline().split())))
# prefix sum table    
S = []
for i in range(n+1):
    S.append([0]*(n+1))
# prefix sum table 구성    
for i in range(1, n+1):
    for j in range(1, n+1):
        S[i][j] = S[i-1][j] + S[i][j-1] - S[i-1][j-1] + table[i-1][j-1]

# 원하는 구간의 합 구하기
for i in range(m):
    a, b, c, d = map(int, sys.stdin.readline().split())
    ans = S[c][d] - S[a-1][d] - S[c][b-1] + S[a-1][b-1]
    print(ans)