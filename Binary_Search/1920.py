import sys

n = int(sys.stdin.readline().rstrip())

a = list(map(int, sys.stdin.readline().split()))

m = int(sys.stdin.readline().rstrip())

b = list(map(int, sys.stdin.readline().split()))

# binary search를 위한 정렬
a.sort()

# binary search
def binary_search(array, target, s, e):
	if s > e:
		return None
	
	mid = (s + e) // 2
	if array[mid] == target:
		return True
	
	if array[mid] > target :
		return binary_search(array, target, s, mid-1)
	else :
		return binary_search(array, target, mid+1, e)
	
for i in b :
	if binary_search(a, i, 0, n-1):
		print(1)
	else :
		print(0)