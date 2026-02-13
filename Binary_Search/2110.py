import sys

n, c = map(int, sys.stdin.readline().split())

house = []
for i in range(n):
    house.append(int(sys.stdin.readline().strip()))
house.sort()

def install(dist):
    # 일단 첫 집은 고르고 시작
    count = 1
    last = house[0]
    
    # 만약 최소 거리 dist보다 크거나 같으면
    for i in range(1, n):
        if house[i] - last >= dist:
            count += 1
            last = house[i]
    # count가 c보다 크거나 같으면 true를 리턴
    return count >= c
# 문제 조건상 가능한 최소 거리
left = 1
# 문제 조건상 가능한 최대 거리
right = house[-1] - house[0]
answer = 0
while (left <= right):
    mid = (left + right) // 2
    if install(mid):
        answer = mid
        left = mid + 1
    else:
        right = mid - 1
        
print(answer)