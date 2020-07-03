#import sys
#input = sys.stdin.readline
def main():
    N = int( input())
    for _ in range(N):
        n, k = map( int, input().split())
        A = list( map( int, input().split()))
        B = list( map( int, input().split()))
        A.sort()
        B.sort(reverse=True)
        ans = 0
        for i in range(n):
            if i+1 <= k:
                if A[i] < B[i]:
                    ans += B[i]
                    continue
            ans += A[i]
        print( ans)
if __name__ == '__main__':
    main()


