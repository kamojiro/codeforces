#import sys
#input = sys.stdin.readline
def solve():
    l, r, m = map( int, input().split())
    a = l
    n = (m-(r-l)+a-1)//a
    for x in range(l,r+1):
        if (m-(r-l)+x-1)//x > 0:
            a = x
            n = (m-(r-l)+x-1)//x
            # print("m", x, n, m-n*a)
            if l-r <= m - n*a <= r-l:
                break
        if (m-l+r)//x > 0:
            a = x
            n = (m-l+r)//x
            # print("M", x, n, m-n*a)
            if l-r <= m - n*a <= r-l:
                break
    e = m-a*n
    # print(n,a, e)
    for b in range(l,r+1):
        if l <= b-e and b-e <= r:
            c = b-e
            return " ".join(map(str, [a,b,c]));

def main():
    T = int( input())
    ANS = [ solve() for _ in range(T)]
    print( "\n".join( map( str, ANS)))
if __name__ == '__main__':
    main()
