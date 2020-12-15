sum = 0
arr = []
while(sum >= 0):
    n = int(input())
    sum += n
    if(sum >= 0):
        arr.append(n)

for i in arr:
    print(i)
