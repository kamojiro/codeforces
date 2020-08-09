#import sys
#input = sys.stdin.readline

def solve_two(A, n, m):
    B = [ (A[0][i] + A[1][i])%2 for i in range(m)]
    odd = 0
    even = 0
    for i in range(m):
        if B[i] == i%2:
            odd += 1
        else:
            even += 1
    return min(odd, even)

def solve_three(A, n, m):
    BU = [ (A[0][i] + A[1][i])%2 for i in range(m)]
    BD = [ (A[1][i] + A[2][i])%2 for i in range(m)]
    # print(BU)
    # print(BD)
    oddodd = 0
    oddeven = 0
    evenodd = 0
    eveneven = 0
    for i in range(m):
        if BU[i] == i%2:
            oddeven += 1
            oddodd += 1
        else:
            eveneven += 1
            evenodd += 1
        if BD[i] == i%2:
            if BU[i] == i%2:
                evenodd += 1
            else:
                oddodd += 1
        else:
            if BU[i] == i%2:
                eveneven += 1
            else:
                oddeven += 1
    # print(oddodd, oddeven, evenodd, eveneven)
    return min([oddodd, oddeven, evenodd, eveneven])

def solve():
    n, m = map( int, input().split())
    A = [ list( map( int, list( input()))) for _ in range(n)]
    if n >= 4 and m >= 4:
        return -1
    if n == 1:
        return 0
    if n > m:
        n, m = m, n
        A = list( zip(*A))
    ans = 0
    if n == 2:
        return solve_two(A,n,m)
    if n == 3:
        return solve_three(A,n,m)
    
        
        
def main():
    # t = int( input())
    # ANS = [ solve() for _ in range(t)]
    print(solve())
if __name__ == '__main__':
    main()
