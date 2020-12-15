def check(arr=[]):
    idx = 0
    while idx + 1 < len(arr) and arr[idx + 1] < arr[idx]:
        idx += 1
    while idx + 1 < len(arr) and arr[idx + 1] > arr[idx]:
        idx += 1
    if idx == len(arr) - 1:
        return 1
    return 0


n = int(input())
arr = []
for i in range(n):
    x = int(input())
    arr.append(x)

if check(arr):
    print("true")
else:
    print("false")
