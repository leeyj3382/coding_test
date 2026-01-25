import sys

n = int(sys.stdin.readline())
array = list(map(int, sys.stdin.readline().split()))
x = int(sys.stdin.readline())

array.sort()
count = 0
left, right  = 0, n-1

while left < right :
	s = array[left] + array[right]
	if s == x:
		count += 1
		left += 1
		right -= 1
	elif s < x:
		left += 1
	else :
		right -= 1
		
print(count)