t = int(input())

for tc in range(t):
    n = int(input())
    coins = list(map(int, input().split()))
    m = int(input())
    
    # 0원부터 m원 까지의 dp테이블
    d = [ 0 for i in range(m+1)]
    # 동전을 고르지 않는다는 경우의 ㅅ ㅜ
    d[0] = 1
    
    # i원까지 도달할 수 있는 경우의 수
    for coin in coins:
        for i in range(coin, m+1):
            d[i] += d[i-coin]
    print(d[m])