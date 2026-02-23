import sys

n, m = map(int, sys.stdin.readline().split())

never_heard = {sys.stdin.readline().strip() for _ in range(n)}
never_saw = {sys.stdin.readline().strip() for _ in range(m)}

result = sorted(never_heard & never_saw)

print(len(result))
print('\n'.join(result))