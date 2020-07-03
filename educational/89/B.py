#import sys
#input = sys.stdin.readline
def solve():
    n, x, m = map( int, input().split())
    LR = [ tuple(map( int, input().split())) for _ in range(m)]
    a = x
    b = x
    for l, r in LR:
        if (l <= a and a <= r) or ( a <= l and l <= b):
            a = min(l, a)
            b = max(r, b)

    return b-a+1
    
def main():
    T = int( input())
    for _ in range(T):
        print(solve())
if __name__ == '__main__':
    main()
