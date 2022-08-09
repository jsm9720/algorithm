import sys

N, M, K = map(int, sys.stdin.readline().split())
arr = list(map(int,sys.stdin.readline().split()))

arr.sort()

sol = 0
count = 0
for i in range(M):
    if count > K:
        sol += arr[-2]
        count == 0
    else:
        sol += arr[-1]
print(sol)
