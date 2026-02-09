import sys

n = int(sys.stdin.readline())

data = list(map(int, sys.stdin.readline().split()))
# dp테이블 : 초기값은 1
d = [1] * (n)
# 맨 처음 원소는 1이 최대 길이임.
for i in range(1, n):
    for j in range(i):
        if data[j] < data[i]:
            # 나보다 작은 녀석이 나올 때마다 확인
            d[i] = max(d[i], d[j]+1)
            
print(max(d))