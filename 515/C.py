q = int( input())
LC = dict()
RC = dict()
L, R = 0, 0
for _ in range(q):
    w, ix = input().split()
    if w == 'R':
        RC[ix] = R
        LC[ix] = -1
        R += 1
    elif w == 'L':
        LC[ix] = L
        RC[ix] = -1
        L += 1
    else:
        if LC[ix] == -1:
            print( min( L+RC[ix], R-1 - RC[ix]))
        else:
            print( min( R + LC[ix], L-1 - LC[ix]))
