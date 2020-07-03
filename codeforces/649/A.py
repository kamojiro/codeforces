#import sys
#input = sys.stdin.readline
def solve():
    n, x = map( int, input().split())
    A = list( map( lambda y: int(y)%x, input().split()))
    for a in A:
        if a != 0:
            break
    else:
        return -1
    s = sum(A)
    if s%x != 0:
        return n
    begin = 0
    end = 0
    for i in range(n):
        if A[i] != 0:
            begin = i+1
            break
    for i in range(n-1,-1,-1):
        if A[i] != 0:
            end = n-i
            break
    return n - min(begin, end)
def main():
    t = int( input())
    for _ in range(t):
        print( solve())
if __name__ == '__main__':
    main()
