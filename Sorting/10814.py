# n = int(input())

# array = []
# for i in range(n):
# 	array.append(list((input().split())))

# for i in range(n):
# 	array[i][0] = int(array[i][0])
	
# array = sorted(array, key = lambda x : (x[0]))

# for arr in array:
# 	for a in arr:
# 		print(a, end = ' ')
# 	print()



import sys

n = int(sys.stdin.readline())

array = []
for i in range(n):
	array.append(list(sys.stdin.readline().split()))
	
for i in range(n):
	array[i][0] = int(array[i][0])
	
array.sort(key=lambda x: x[0])

for arr in array:
	print(arr[0], arr[1])