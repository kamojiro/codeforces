#import sys
#input = sys.stdin.readline
def solve():
    a, b, c, d = map( int, input().split())
    if a <= b:
        print(b)
        return
    if c - d <= 0:
        print(-1)
        return
    print(b+((a-b)+(c-d)-1)//(c-d)*c)
    return

def main():
    t = int( input())
    for _ in range(t):
        solve()
if __name__ == '__main__':
    main()
