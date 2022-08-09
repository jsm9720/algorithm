import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

arr.sort()

cnt = 0
while True:
    print(arr)
    if len(arr) >= arr[-1]:
        arr = arr[:len(arr)-arr[-1]]
        cnt += 1
    else:
        arr.pop()
    
    if len(arr) <= 0:
        break

print(cnt)
