import sys
m, n, l = map(int,sys.stdin.readline().split())
# 사대 위치
shot = list(map(int, sys.stdin.readline().split()))
# 오름차순 정렬
shot.sort()
# 동물 좌표를 저장
animal = []
for i in range(n):
    animal.append(tuple(map(int, sys.stdin.readline().split())))

result = 0
for ani in animal:
    x, y = ani
    r = l - y
    if r < 0:
        continue
    # |x-a| <= L-b
    # -r <= x-a <= r
    # a-r <= x <= r+a
    left = 0
    right = m - 1
    lower_bound = x - r
    upper_bound = x + r
    while(left <= right):
        mid = (left + right) // 2
        
        if shot[mid] < lower_bound:
            left = mid + 1
        elif shot[mid] > upper_bound:
            right = mid - 1
        else:
            result += 1
            break
            
print(result)
    
            
    