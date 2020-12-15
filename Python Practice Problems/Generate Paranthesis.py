def func(ob, cb, n, s=[]):
    if(cb == n):
        print(''.join(s))
        return
    else:
        if(ob > cb):
            s.append(')')
            func(ob, cb + 1, n, s)
            s.pop()
        if(ob < n):
            s.append('(')
            func(ob + 1, cb, n, s)
            s.pop()
    return


n = int(input())
func(0, 0, n)
