from collections import deque

def answer0(A,B,C):
    ans = 0
    for x, y in A:
        ans += x*y
    for x, y in B:
        ans += x*y
    for x, y in C:
        ans += x*y
    return ans


def answer(A,B,C,LA,LB,LC,MAB, MBC):
    ia = 0
    ib = 0
    ic = 0
    ret = 0
    ab = 0
    bc = 0
    while True:
        if ia < LA :
            a = A[ia]
        if ib < LB:
            b = B[ib]
        if ic < LC:
            c = C[ic]
        if (a == 0 and b == 0) or ( c == 0 and b == 0) or ( c == 0 and a == 0):
            break
        if a >= c and b >= c and ab < MAB:
            ret += a*b
            ia += 1
            ib += 1
            a = 0
            b = 0
            ab += 1
        elif b >= a and c >= a and bc < MBC:
            ret += b*c
            ic += 1
            ib += 1
            b = 0
            c = 0
            bc += 1
        else:
            ret += c*a
            ic += 1
            ia += 1
            c = 0
            a = 0
    return ret

def greed(Rs,Gs,Bs,R,G,B):
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
        return answer0(RG,GB,BR)
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
    return ans + answer0(RG,GB,BR)


def main():
    R, G, B = map( int, input().split())
    Rs = list( map( int, input().split()))
    Gs = list( map( int, input().split()))
    Bs = list( map( int, input().split()))

    Rs.sort(reverse=True)
    Gs.sort(reverse=True)
    Bs.sort(reverse=True)
    RG = min(R, G)
    GB = min(G, B)
    BR = min(B,R)
    ans = greed(Rs,Gs,Bs,R,G,B)
    for rg in range(RG+1):
        if GB < rg:
            break
        for gb in range(GB-rg+1):
            h = answer(Rs, Gs, Bs, R,G,B,rg,gb)
            if h > ans:
                ans = h
    print(ans)
if __name__ == '__main__':
    main()
