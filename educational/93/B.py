#import sys
#input = sys.stdin.readline
def solve():
    S = list( map( int, list( input())))
    S.append(0)
    now = 0
    ONE = []
    for s in S:
        if s == 1:
            now += 1
        else:
            if now > 0:
                ONE.append(now)
            now = 0
    ONE.sort(reverse=True)
    return sum( ONE[::2])
    
def main():
    t = int( input())
    ANS = [ solve() for _ in range(t)]
    print("\n".join( map(str, ANS)))
if __name__ == '__main__':
    main()
