import math


def val(): return int(input().rstrip())


for _ in range(val()):
    A = val()
    ans = set()
    for i in range(0,  int(math.sqrt(A)) + 2):
        tmp = A - i * i
        if tmp < 0:
            continue
        if int(math.sqrt(tmp)) ** 2 == tmp:
            mn = min(i, int(math.sqrt(tmp)))
            mx = max(i, int(math.sqrt(tmp)))
            ans.add((mn, mx))
    final = list(ans)
    final.sort()
    for i in final:
        print("({},{})".format(i[0], i[1]), end=" ")
    print()
