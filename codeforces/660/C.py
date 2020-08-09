#import sys
#input = sys.stdin.readline
from collections import deque
def solve():
    n, m = map( int, input().split())
    P = list( map( int, input().split()))
    H = list( map( int, input().split()))
    E = [[] for _ in range(n)]
    for _ in range(n-1):
        x, y = map( lambda x: int(x)-1, input().split())
        E[x].append(y)
        E[y].append(x)
    parent = [0]*n
    d = deque([0])
    V = [False]*n
    V[0] = True
    C = []
    while d:
        v = d.popleft()
        C.append(v)
        for w in E[v]:
            if not V[w]:
                d.append(w)
                V[w] = True
                parent[w] = v
    AP = [p for p in P]
    for v in C[::-1]:
        if v == 0:
            continue
        AP[parent[v]] += AP[v]

    no = "NO"
    G = [0]*n
    B = [0]*n
    for i in range(n):
        h, p = H[i], AP[i]
        if (h+p)%2 == 0 and p-h >= 0 and h+p >= 0:
            G[i] = (h+p)//2
            B[i] = (p-h)//2
        else:
            return no
    V = [False]*n
    V[0] = True
    for v in C:
        good = 0
        bad = 0
        for w in E[v]:
            if not V[w]:
                good += G[w]
                # else:
                #     bad += -H[w]
                V[w] = True
        if good > G[v]:
            return no
        
    return "YES"


def main():
    t = int( input())
    ANS = [ solve() for _ in range(t)]
    print( "\n".join( ANS))

if __name__ == '__main__':
    main()
