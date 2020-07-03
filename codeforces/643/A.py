import sys
input = sys.stdin.readline

def digit(n):
    t = list( map( int, list( str(n))))
    return max(t)*min(t)

def solve():
    a, K = map(int, input().strip().split())
    for _ in range(K-1):
        if digit(a) == 0:
            return a
        a += digit(a)
    return a
def main():
    T = int( input())
    ANS = []
    for _ in range(T):
        ANS.append( solve())
    print( "\n".join( map( str, ANS)))
if __name__ == '__main__':
    main()
