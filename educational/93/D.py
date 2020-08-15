#import sys
#input = sys.stdin.readline
from collections import deque

def answer(A,B,C):
    ans = 0
    for x, y in A:
        ans += x*y
    for x, y in B:
        ans += x*y
    for x, y in C:
        ans += x*y
    return ans

def main():
    R, G, B = map( int, input().split())
    Rs = list( map( int, input().split()))
    Gs = list( map( int, input().split()))
    Bs = list( map( int, input().split()))

    Rs.sort(reverse=True)
    Gs.sort(reverse=True)
    Bs.sort(reverse=True)
    Rs = deque(Rs)
    Gs = deque(Gs)
    Bs = deque(Bs)
    RG = []
    GB = []
    BR = []
    r = 0
    g = 0
    b = 0
    while True:
        if r == 0 and Rs:
            r = Rs.popleft()
        if g == 0 and Gs:
            g = Gs.popleft()
        if b == 0 and Bs:
            b = Bs.popleft()
        if (r == 0 and g == 0) or ( g == 0 and b == 0) or ( b == 0 and r == 0):
            break
        if r >= b and g >= b:
            RG.append((r,g))
            r = 0
            g = 0
        elif g >= r and b >= r:
            GB.append((g,b))
            g = 0
            b = 0
        else:
            BR.append((b,r))
            b = 0
            r = 0

    if r > 0:
        Rs.appendleft(r)
    if g > 0:
        Gs.appendleft(g)
    if b > 0:
        Bs.appendleft(b)
    # print(Rs, Gs, Bs)
    if Rs:
        K = Rs
        KK = GB
    elif Bs:
        K = Bs
        KK = RG
    elif Gs:
        K = Gs
        KK = BR
    else:
        print( answer(RG,GB,BR))
        return
    print( "first", answer(RG,GB,BR))
    t = 0
    L = len(KK)
    M = len(K)
    p = 0
    ans = 0
    # print(K, KK)
    while p < M-1:
        k0 = K[p]
        k1 = K[p+1]
        for i in range(t,L):
            a, b = KK[i]
            if a < b:
                a, b = b,a
            if k0*a + k1*b > a*b:
                KK[i] = (0,0)
                ans += k0*a + k1*b
                p += 2
                t = i+1
                break
        else:
            p += 1
    print( ans, answer(RG,GB,BR))
    print( ans + answer(RG,GB,BR))
    
if __name__ == '__main__':
    main()
