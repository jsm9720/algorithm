import sys

n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

cnt = 0
for i in range(n):
    for j in range(i+1,n):
        if arr[i] != arr[j]:
            cnt += 1

print(cnt)
