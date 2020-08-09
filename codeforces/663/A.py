#import sys
#input = sys.stdin.readline
def main():
    t = int( input())
    for _ in range(t):
        print(" ".join(map( str, [i+1 for i in range( int( input()))])))
if __name__ == '__main__':
    main()
