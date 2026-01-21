data = input()

target = [ 1, 2, 3, 4, 5, 6, 7, 8]
data_ = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
count = 8

x, y = 0, 0

for i in range(8):
	if (data[0] == data_[i]):
		x = int(data[1])
		y = i+1
		
inrange = [[x-2,y-1], [x-2,y+1], [x-1,y+2], [x+1,y+2], [x+2,y-1], [x+2,y+1], [x-1,y-2], [x+1,y-2]]


for loc in inrange:
	for i in loc:
		if (i > 8) or (i < 1) :
				count -= 1
				print(count)
				break

print(count)