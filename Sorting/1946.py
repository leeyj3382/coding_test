import sys

t = int(sys.stdin.readline())


for i in range(t):
	n = int(sys.stdin.readline())
	candidates = []
	for j in range(n):
		candidates.append(list(map(int, sys.stdin.readline().split())))
	candidates.sort(key = lambda x : x[0])
	
	count = 0
	best_interview = 10**9 # 큰 더미 값
	
	for _, interview in candidates:
		
		if interview < best_interview:
			count += 1
			best_interview = interview
	
	print(count)