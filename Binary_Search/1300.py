import sys

n = int(sys.stdin.readline().strip())
k = int(sys.stdin.readline().strip())

l, r = 1, k
ans = k

while l <= r:
    m = (l + r) // 2
    
    # m 이하가 몇개인지 세기
    cnt = 0
    # 각 행에서
    for i in range(1, n+1):
        # mid 이하인 녀석의 개수를 가산
        cnt += min(n, m//i)
        
    if cnt >= k:
        ans = m
        r = m - 1
    else:
        l = m + 1
        
print(ans)