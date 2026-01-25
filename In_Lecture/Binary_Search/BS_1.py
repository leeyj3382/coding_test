import sys


# 떡 자르기 및 개수 리턴
def cut(a, loc):
	count = 0
	for i in range(n):
		if a[i] > loc :
			count += (a[i]-loc)
	print(count)
	return count

def binary_search(array, target, start, end):

	if start > end :
		return None
	
	mid = (end + start)//2
	b = cut(array, mid)
	
	if b == target :
		return mid
		
	if b > target :
		return binary_search(array, target, start, mid-1)
	else:
		return binary_search(array, target, mid+1, end)
		

n, m = map(int, sys.stdin.readline().split())

# 이 반복문의 최대 연산 횟수는 약 1,000,000이라 시간 내 수행 가능
a = list(map(int, sys.stdin.readline().split()))

print(binary_search(a, m, 0, max(a)))


		