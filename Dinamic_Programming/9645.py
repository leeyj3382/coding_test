t = int(input())

for tc in range(t):
    n = int(input())
    # 위쪽 스티커
    top = list(map(int, input().split()))
    # 아래쪽 스티커
    bottom = list(map(int, input().split()))
    # dp 테이블은 d[col][0-선택 안함, 1-위쪽 선택, 2-아래쪽 선택]로 정의
    d = []
    for i in range(n):
        d.append(list( 0 for i in range(3)))
    
    d[0][0] = 0
    d[0][1] = top[0]
    d[0][2] = bottom[0]
    for col in range(1, n):
        # 이번 열에서 떼지 않는다면
        d[col][0] = max(d[col-1][0], d[col-1][1], d[col-1][2])
        # 이번 열에서 위에 녀석을 뗀다면
        d[col][1] = max(d[col-1][0], d[col-1][2]) + top[col]
        # 이번 열에서 아래 스티커를 뗀다면
        d[col][2] = max(d[col-1][0], d[col-1][1]) + bottom[col]
    print(max(d[n-1][0], d[n-1][1], d[n-1][2]))  