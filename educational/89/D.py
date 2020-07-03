#import sys
#input = sys.stdin.readline
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def solve(a):
    if a == 1:
        return [-1,-1]
    p = -1
    q = a
    for i in range(2, int(a**(1/2))+1):
        if q%i == 0:
            while q%i == 0:
                q //= i
            p = i
            break
    if p == -1 or q == 1:
        return [-1,-1]
    if gcd(a, p+q) > 1:
        return [-1,-1]
    else:
        return( p, q)

def main():
    N = int( input())
    A = list( map( int, input().split()))
    C = [0]*N
    D = [0]*N
    for i in range(N):
        C[i], D[i] = solve(A[i])
    print(" ".join( map( str, C)))
    print(" ".join( map( str, D)))
if __name__ == '__main__':
    main()
