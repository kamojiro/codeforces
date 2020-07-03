#import sys
#input = sys.stdin.readline
def main():
    now = 0
    h, c, t = map( int, input().split())
    for n in range(1000000):
        now = ((n+1)*h+n*c)/(2*n+1)
        if n%10000 == 0:
            print(n, now, abs(t-now))
if __name__ == '__main__':
    main()

#1000000 0 500001

