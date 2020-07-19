#import sys
#input = sys.stdin.readline
from heapq import heapify, heappush, heappop
def main():
    n = int( input())
    A = list( map( int, input().split()))
    if n == 1:
        print(A[0])
        return
    B = [i-1 for i in range(n)]
    B[0] = n-1
    F = [i+1 for i in range(n)]
    F[-1] = 0
    h = [ (A[i],i) for i in range(n)]
    heapify(h)
    V = [True]*n
    while h:
        # print(h)
        a, i = heappop(h)
        if not V[i]:
            continue
        if A[i] != a:
            continue
        b = B[i]
        f = F[i]
        # print(V)
        # print("BF",B,F)
        # print(b,V[b], f, V[f])
        if (not V[b]) or (not V[f]):
            continue
        A[i] = A[b] + A[f]
        heappush(h, (A[i],i))
        V[b] = False
        V[f] = False
        bb = B[b]
        ff = F[f]
        B[i] = bb
        F[i] = ff
        F[bb] = i
        B[ff] = i
        # print("done")
    for i in range(n):
        if V[i]:
            print(A[i])
            return
        
        
        
    
if __name__ == '__main__':
    main()
