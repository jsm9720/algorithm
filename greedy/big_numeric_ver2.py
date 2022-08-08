import sys

_, M, K = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

arr.sort()

tmp = M // (K + 1)
print(arr[-2] * tmp + arr[-1] * (M - tmp))
