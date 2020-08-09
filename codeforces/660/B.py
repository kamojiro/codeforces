#import sys
#input = sys.stdin.readline
def solve():
    n = int( input())
    m = n//4
    if n%4 == 0:
        return "9"*(n-m) + "8"*m
    else:
        return "9"*(n-m-1)+"8"*(m+1)

def main():
    t = int( input())
    ANS = [ solve() for _ in range(t)]
    print( "\n".join(ANS))
if __name__ == '__main__':
    main()
