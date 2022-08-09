import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

arr.sort()

cnt = 0
tmp = 0
for i in arr:
    tmp += 1
    if tmp >= i:
        cnt += 1
        tmp = 0

print(cnt)
