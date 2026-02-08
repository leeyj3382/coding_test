import sys

n = int(sys.stdin.readline())

data = list(map(int, sys.stdin.readline().split()))
# dp테이블
d = [0] * (n)
# 초기값 설정
d[0] = 1
if data[0] < data[1]:
    d[1] = 2
else:
    d[1] = 1
for i in range(2, n):
    # 만약 앞 원소보다 작으면
    if data[i] < data[i-1]:
        # 앞 앞 원소에 이어서 가는게 베스트
        d[i] = d[i-2]+1
    # 앞 원소랑 같으면, 현상 유지
    elif data[i] == data[i-1]:
        d[i] = d[i-1]
    else:
        # 앞 원소보다 크면 => 점화식
        d[i] = max(d[i-2]+1, d[i-1]+1)
        
print(max(d))