#import sys
#input = sys.stdin.readline
def solve():
    n, m = map( int, input().split())
    A = [ list( map( int, input().split())) for _ in range(n)]
    if n > m:
        n, m = m, n
        A = list( zip(*A))
    T = []
    for i in range(n-1):
        S = [0,0]
        for j in range(i+1):
            S[A[i-j][j]] += 1
        T.append(S)
    for i in range(m-n):
        S = [0,0]
        for j in range(n):
            S[A[j][n-1+i-j]] += 1
        T.append(S)
    for i in range(n):
        S = [0,0]
        for j in range(n-i):
            # print(i+j, m-1-j)
            S[A[i+j][m-1-j]] += 1
        T.append(S)
    # print(T)
    ret = 0
    for i in range((n+m-1)//2):
        zero = T[i][0] + T[-1-i][0]
        one = T[i][1] + T[-1-i][1]
        ret += min(one, zero)
    return ret
    
def main():
    T = int( input())
    for _ in range(T):
        print(solve())
if __name__ == '__main__':
    main()
