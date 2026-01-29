n = int(input())
array = list(map(int, input().split()))
# 순서를 뒤집어 '최장 증가 부분 순열' 문제로 변환
array.reverse()

# 다이나믹 프로그래밍을 위한 1차원 DP 테이블 초기화
dp = [1] * n

# 가장 긴 증가하는 부분 순열(LIS) 알고리즘 수행
for i in range(1, n):
	for j in range(0, i):
		if array[j] < array[i] :# 이전 녀석보다 크면 부분 순열이 연결되기 때문에,
			dp[i] = max(dp[i], dp[j]+1)# dp[j] + 1을 하는 거임.
			
# 열외해야 하는 병사의 최소 수를 출력
print(n - max(dp))