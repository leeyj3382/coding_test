import sys

n, m = map(int, sys.stdin.readline().split())

a = list(map(int, sys.stdin.readline().split()))


def binary_search(a, t, s, e):
	result = 0
	while (s <= e):
		total = 0
		mid = (s + e)//2
		
		for i in a:
			if i > mid :
				total += (i-mid)
		if total >= t :
			result = mid
			s = mid + 1
		elif total < t:
			e = mid - 1
			
	return result
		
print(binary_search(a, m, 0, max(a)))