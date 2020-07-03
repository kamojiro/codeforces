#import sys
#input = sys.stdin.readline
def main():
    t = int( input())
    for _ in range(t):
        x, y = map( int, input().split())
        a, b = map( int, input().split())
        print( min([min(x,y)*b + (max(x,y)-min(x,y))*a, (x+y)*a]))
if __name__ == '__main__':
    main()
