import sys
input = sys.stdin.readline
from collections import Counter

def solve():
    n, m, x, y = map( int, input().split())
    A = [ input().strip() for _ in range(n)]
    if x*2 <= y:
        return Counter("".join(A))["."]*x
    ans = 0
    for i in range(n):
        now = 0
        for j in range(m):
            if A[i][j] == "*":
                if now == 1:
                    ans += x
                now = 0
                continue
            if now == 0:
                now += 1
            else:
                now = 0
                ans += y
        if now == 1:
            ans += x
    return ans


def main():
    T = int( input())
    for _ in range(T):
        print( solve())
if __name__ == '__main__':
    main()
