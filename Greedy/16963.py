a, b = map(int, input().split())

# 출력이 최솟값 + 1
count = 1

while b > a :
	if b % 10 == 1:
		# b에서 1을 빼고 10으로 나눈 몫을 취하나
		# 바로 10으로 나눈 몫을 취하나 동일함
		b //= 10
		count += 1
		
	elif b % 2 == 0:
		b //= 2
		count += 1
		
	else :
		count = -1
		break
		
print(count if b == a else -1)