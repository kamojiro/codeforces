#import sys
#input = sys.stdin.readline
Q = 10**9+7
def main():
    n, m, q = map( int, input().split())
    UVW = [ tuple( map( int, input().split())) for _ in range(m)]
    ans = 0
    V = [-1]*(n+1)
    V[1] = 0
    for _ in range(2000):
        W = [-1]*(n+1)
        for n, m, w in UVW:
            if V[n] != -1:
                W[m] = max(W[m], V[n]+w)
            if V[m] != -1:
                W[n] = max(W[n], V[m]+w)
        V = W
        ans += max(V)
        ans %= Q
    
if __name__ == '__main__':
    main()
