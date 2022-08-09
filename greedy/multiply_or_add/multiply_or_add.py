import sys

# arr = list(map(int, sys.stdin.readline().rstrip().lstrip('0')))
arr = list(map(int, sys.stdin.readline().rstrip()))

result = arr[0]
for i in arr[1:]:
    if i <= 1 or result <= 1:
        result += i
    else:
        result *= i

print(result)
