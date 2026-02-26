import sys
sys.setrecursionlimit(10**7)

n, s = map(int, sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().split()))
result = 0
def dfs(i, total):
    global result
    if i == n:
        if total == s:
            result += 1
        return
    
    dfs(i+1, total + data[i])
    dfs(i+1, total)
if s == 0:
    result -= 1
dfs(0,0)
print(result)