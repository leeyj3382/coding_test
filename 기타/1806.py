import sys
INF = int(1e9)
n, s = map(int, sys.stdin.readline().split())

table = list(map(int, sys.stdin.readline().split()))

# 포인터 초기화
end = 0
# 최소 길이를 담을 변수
count = INF
# 구간 합
interval_sum = 0
# start를 옮기기 위한 반복문
for start in range(n):
    # end를 가능한 만큼 오른쪽으로 한칸씩 이동
    while interval_sum < s and end < n:
        interval_sum += table[end]
        end += 1
    # interval_sum이 s와 같으면, count값과 비교해서 최소 값으로
    if interval_sum >= s:
        count = min(count, end - start)
    # 지금 start 포인터가 가르키는 녀석을 빼서 start를 옮길 준비
    interval_sum -= table[start]

print(count if count != INF else 0)