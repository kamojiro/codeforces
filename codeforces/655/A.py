#import sys
#input = sys.stdin.readline
def main():
    t = int( input())
    N = [ int( input()) for _ in range(t)]
    for n in N:
        print( " ".join(["1"]*n))
if __name__ == '__main__':
    main()
