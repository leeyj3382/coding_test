import sys
sys.setrecursionlimit(10**7)


def dfs(start, path):
    if len(path) == 6:
        print(*path)
        return
    for i in range(start, k):
        path.append(nums[i])
        dfs(i+1, path)
        path.pop()

while True:
    a = list(map(int, sys.stdin.readline().split()))
    if a[0] == 0:
        break
    k = a[0]
    nums = a[1:]
    
    dfs(0, [])
    print()

        