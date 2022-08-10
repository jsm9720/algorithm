import sys

n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

weight_info = [0]*(m+1)

for i in arr:
    weight_info[i] += 1

cnt = 0
for j in weight_info[1:]:
    n = n - j
    cnt += n * j

print(cnt)
