n = int(input())

x = 1
y = 1

data = list(map(str, input().split()))

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

for move in data:
	if move == 'L':
		x_ = x + dx[2]
		y_ = y + dy[2]
	elif move == 'R':
		x_ = x + dx[0]
		y_ = y + dy[0]
	elif move == 'U':
		x_ = x + dx[1]
		y_ = y + dy[1]
	else :
		x_ = x + dx[3]
		y_ = y + dy[3]
	if (x_ > n or y_ > n) or(x_ < 1 or y_ < 1):
		continue
	x = x_
	y = y_

print(x, y)
