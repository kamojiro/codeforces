#import sys
#input = sys.stdin.readline
def main():
    A, B, C, D = map( int, input().split())
    ans = 0
    for x in range(C, D+1):
        if C-x+1 < B:
            ans += (C-B+1)
if __name__ == '__main__':
    main()
