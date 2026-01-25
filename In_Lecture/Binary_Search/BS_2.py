from bisect import bisect_left, bisect_right

n, x = map(int, input().split())

a = list(map(int, input().split()))

left_index = bisect_left(a, x)
right_index = bisect_right(a, x)

if right_index - left_index != 0:
	print(right_index - left_index)
else :
	print(-1)