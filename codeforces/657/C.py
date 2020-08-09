#import sys
#input = sys.stdin.readline
def solve():
    n, m = map( int, input().split())
    AB = [ tuple( map( int, input().split())) for _ in range(m)]
    BA = [(-a,b,i) for a, b in AB]
    BA.sort()
    
    

def main():
    t = int( input())
    ANS = [ solve() for _ in range(t)]
    print( "\n".join( map( str, ANS)))
if __name__ == '__main__':
    main()
