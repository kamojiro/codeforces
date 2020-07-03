import sys
input = sys.stdin.readline

def solve():
    N = int( input())
    A = list( map( int, input().strip().split()))
    A.sort()
    ans = 0
    now = 0
    m = 0
    C = []
    for a in A:
        now += 1
        if m < a:
            m = a
        if now >= m:
            ans += 1
            C.append(now)
            m = 0
            now = 0
    return ans

def main():
    T = int( input())
    ANS = []
    for _ in range(T):
        ANS.append( solve())
    print('\n'.join( map( str, ANS)))
if __name__ == '__main__':
    main()
