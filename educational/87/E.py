import sys
input = sys.stdin.readline
from collections import Counter, deque, defaultdict

def find(A,x):
    p = A[x]
    if p == x:
        return x
    a = find(A,p)
    A[x] = a
    return a
 
def union(A, x, y):
#    bx, by = sorted([find(A,x), find(A,y)]) # bx, by = find(A,x), find(A,y)だと無限ループ。
    if find(A,x) > find(A,y):
        bx, by = find(A,y), find(A,x)
    else:
        bx, by = find(A,x), find(A,y)
    A[y] = bx
    A[by] = bx


def main():
    N, M = map( int, input().split())
    nums = list( map( int, input().split()))
    E = [[] for _ in range(N)]
    U = [i for i in range(N)]
    for _ in range(M):
        u, v = map( lambda x: int(x)-1, input().split())
        E[u].append(v)
        E[v].append(u)
        union(U,u,v)
    T = set()
    for i in range(N):
        T.add( find(U,i))
    T = list(T)
    V = [-1]*N
    d = deque()
    for t in T:
        V[t] = 0
        d.append(t)

    while d:
        u = d.popleft()
        t = V[0]^1
        for v in E[u]:
            if V[v] == -1:
                V[v] = t
            else:
                if V[v] != t:
                    print("NO")
                    return
                
    e = defaultdict( lambda : [0,0])
    for i in range(N):
        e[find(U,i)][V[i]] += 1
    n2 = nums[1]
    X = [False]*(n2+1)
    X[0] = True
    S = []
    S.append([True]+[False]*n2)
    for t in T:
        w, b = e[t]
        Z = [False]*(n2+1)
        for i in range(n2):
            if X[i]:
                if i+w <= n2:
                    Z[i+w] = True
                if i+b <= n2:
                    Z[i+b] = True
        S.append(Z)
        X = Z
    
    if S[-1][n2]:
        print("YES")
    else:
        print("NO")
        return
    
        
    # C = Counter(V)
    # if nums[0]+nums[2] == C[0]:
    #     print("YES")
    #     ANS = [2]*N
    #     n1 = nums[0]
    #     n2 = nums[2]
    #     for i in range(N):
    #         if V[i] == 0:
    #             if n1 > 0:
    #                 ANS[i] = 1
    #             else:
    #                 ANS[i] = 3
    #     print("".join( map(str, ANS)))
    #     return
    # if nums[0]+nums[2] == C[1]:
    #     print("YES")
    #     ANS = [2]*N
    #     n1 = nums[0]
    #     n2 = nums[2]
    #     for i in range(N):
    #         if V[i] == 1:
    #             if n1 > 0:
    #                 ANS[i] = 1
    #             else:
    #                 ANS[i] = 3
    #     print("".join( map(str, ANS)))
    #     return
    # print("NO")
    
    
if __name__ == '__main__':
    main()
