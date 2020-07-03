#import sys
#input = sys.stdin.readline
Q = 998244353
def main():
    n, m = map( int, input().split())
    A = list( map( int, input().split()))
    B = list( map( int, input().split()))
    now = n-1
    T = [-1]*(n+1)
    for i in range(m,0,-1):
        b = B[i]
        for j in range(now,-1,-1):
            if A[j] == b:
                if j > 0:
                    T[j-1] = B[i-1]
                now = j-1
                if now < 0:
                    print(-1)
                    return
                break
    ans = 0
    now = 0
    j = 0
    for i in range(n):
        if A[i] == B[j]:
            now += 1

            
        
                
if __name__ == '__main__':
    main()
