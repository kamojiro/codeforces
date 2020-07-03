#import sys
#input = sys.stdin.readline
def main():
    n = int( input())
    A = list( map( int, input().split()))
    B = [-1]*n
    N = 10**6
    now = N
    TB = [True]*N
    if A[0] > 0:
        B[0] = 0
        TB[0] = False
    for i in range(1,n):
        a = A[i]
        ab = A[i-1]
        if ab < a:
            if TB[ab]:
                B[i] = ab
                TB[ab] = False
    TB[A[-1]] = False
    indexb = 0
    for i in range(n):
        if B[i] != -1:
            continue
        for j in range(indexb, N):
            if TB[j]:
                TB[j] = False
                indexb = j+1
                B[i] = j
                break
    indexa = 0
    TA = [True]*N
    for i in range(n):
        TA[B[i]] = False
        for j in range(indexa, N):
            if TA[j]:
                if A[i] != j:
                    print(-1)
                    return
                indexa = j
                break
        
    print(" ".join( map( str, B)))
        
    
if __name__ == '__main__':
    main()
