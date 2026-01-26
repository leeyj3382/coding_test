import sys

n = int(sys.stdin.readline().rstrip())
a = list(map(int, sys.stdin.readline().split()))
a.sort()

result = [0, 0]
best = 10 ** 18

def binary_search(s, e, now):
    global best, result
    while s <= e:
        mid = (s + e) // 2
        sm = now + a[mid]

        if abs(sm) < best:
            best = abs(sm)
            result[0], result[1] = now, a[mid]
            if best == 0:
                return

        if sm > 0:
            e = mid - 1
        else:
            s = mid + 1

for i in range(n - 1):
    binary_search(i + 1, n - 1, a[i])

x, y = sorted(result)
print(x, y)
