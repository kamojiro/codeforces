import sys
input = sys.stdin.readline

from collections import Counter
def main():
    n, m, k = map( int, input().split())
    E = [[] for _ in range(n)]
    for _ in range(m):
        u, v = map( lambda x: int(x)-1, input().split())
        E[u].append(v)
        E[v].append(u)
    stack = [0]
    V = [-1]*n
    V[0] = 0
    cycle = -1
    two = True
    while stack:
        v = stack.pop()
        c = (V[v]+1)%2
        for w in E[v]:
            # if cycle != -1 and V[w] != -1 and root[v] != w and v != 0:
            #     cycle = v
            #     cycleswith = w
            if V[w] == -1 :
                stack.append(w)
                V[w] = c
            else:
                if V[w] != c:
                    two = False
    if two:
        C = Counter(V)
        c = 0
        if C[1] > C[0]:
            c = 1
        ANS = [ i+1 for i in range(n) if V[i] == c ]
        print(1)
        print( " ".join( map( str, ANS[:(k+1)//2])))
        return

    V = [False]*n
    root = [-1]*n
    stack = [0]
    cycle = -1
    cyclewith = -1
    while stack:
        v = stack.pop()
        if not V[v]:
            continue
        V[v] = True
        for w in E[v]:
            if root[w] != v and V[w]:
                cycle = v
                cyclewith = w
                break
            if not V[w]:
                root[w] = v
                stack.append(w)
        if cycle != -1:
            break
    ANS = []
    v = cycle
    print(V)
    c = 0
    while v != cyclewith:
        ANS.append(v)
        v = root[v]
        c += 1
        if c > 10:
            break
        print(v)
    ANS.append(cyclewith)
    t = len(ANS)
    if t <= k:
        print(2)
        print(t)
        print( " ".join( map( str, ANS)))
    else:
        print(1)
        print(" ".join( map( str, ANS[:k+1:2])) )
    
    #     print(stack, V, root)
    # if cycle != -1:
    #     ANS = []
    #     W = [False]*n
    #     v = cycle
    #     while v != -1:
    #         W[v] = True
    #         v = root[v]
    #     w = cyclewith
    #     while w != -1:
    #         ANS.append(w)
    #         if W[w]:
    #             break
    #     v = cycle
    #     while v != w:
    #         ANS.append(v)
    #     print(2)
    #     print( len(ANS))
    #     print( " ".join( map( str, ANS)))
    #     return

    # C = Counter(V)
    # c = 0
    # if C[1] > C[0]:
    #     c = 1
    # ANS = [ i+1 for i in range(n) if V[i] == c ]
    # print(1)
    # print( " ".join( map( str, ANS[:(k+1)//2])))

    
        
if __name__ == '__main__':
    main()
