import sys

_ = input()
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()

check = 1
for i in arr:
    if check < i:
        break
    check += i

print(check)
