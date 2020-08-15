#import sys
#input = sys.stdin.readline
from collections import defaultdict

def solve():
    n = int( input())
    A = list( map( int, list( input())))
    ret = 0
    sa = 0
    d = defaultdict( int)
    d[1] += 1
    # print(n)
    for i in range(n):
        sa += A[i]
        z = sa - i
        ret += d[z]
        d[z] += 1
        # print(ret,z, d)
        
    return ret

def main():
    t = int( input())
    ANS = [ solve() for _ in range(t)]
    print("\n".join( map(str, ANS)))
if __name__ == '__main__':
    main()
