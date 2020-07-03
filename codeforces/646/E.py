import sys
input = sys.stdin.readline
from collections import deque, Counter
def main():
    N = int( input())
    A = []
    B = []
    C = []
    cb = [0,0]
    cc = [0,0]
    for _ in range(N):
        a, b , c = map( int, input().split())
        A.append(a)
        B.append(b)
        C.append(c)
        cb[b] += 1
        cc[c] += 1

    E = [[] for _ in range(N)]
    for _ in range(N-1):
        u, v = map( lambda x: int(x)-1, input().split())
        E[u].append(v)
        E[v].append(u)
    if cb[0] != cc[0]:
        print(-1)
        return
    R = [-1]*N
    V = [-1]*N
    V[0] = A[0]
    d = deque(E[0])
    for v in E[0]:
        R[v] = 0
    T = [0]
    while d:
        v = d.popleft()
        T.append(v)
        V[v] = min(V[R[v]], A[v])
        for w in E[v]:
            if V[w] == -1:
                d.append(w)
                R[w] = v
    RT = T[::-1]
    # print(T,R)
    Hzero = [0]*N
    Hone = [0]*N
    ans = 0
    for v in RT:
        if B[v] != C[v]:
            if B[v] == 0:
                Hzero[v] += 1
            else:
                Hone[v] += 1
        if Hzero[v] > 0 and Hone[v] > 0:
            m = min(Hone[v], Hzero[v])
            ans += m*V[v]*2
            Hzero[v] -= m
            Hone[v] -= m
        if v != 0:
            Hzero[R[v]] += Hzero[v]
            Hone[R[v]] += Hone[v]
        # print(v, H)
    print(ans)
            
    
        
if __name__ == '__main__':
    main()
