import sys

n, m = map(int, sys.stdin.readline().split())
day = []
for i in range(n):
    day.append(int(sys.stdin.readline().strip()))

# pay원 인출로 m번 이하인가?
def pull(pay):
    # 일단 뽑고 시작
    count = 1
    wallet = pay
    # n일 동안의 예정된 지출 내역 순회
    for i in range(n):
        a = day[i]
        # 지금 감당 가능하면
        if wallet >= a:
            wallet -= a
            continue
        # 감당 불가하면 => 남아 있는 돈은 넣고, pay만큼 다시 인출
        elif wallet < a:
            count += 1
            wallet = pay
            # 다시 인출 했는데도 안되면 => 불가능
            if wallet < a:
                return False
            if count > m:
                return False
        wallet -= a
        
    return True

left = 1
right = sum(day)
answer = 0
while (left <= right):
    mid = (left + right) // 2
    if pull(mid):
        answer = mid
        right = mid - 1
    else:
        left = mid + 1
        
print(answer)