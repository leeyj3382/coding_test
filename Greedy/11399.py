
n = int(input())

person_per_time = list(map(int, input().split()))

result = 0
acc = 0

person_per_time.sort()

# for i in range(n):
# 	result = acc + person_per_time[i]
# 	acc += result

for i in range(n):
    result += (n - i) * person_per_time[i]
	
	
print(result)