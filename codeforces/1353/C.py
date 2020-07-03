#import sys
#input = sys.stdin.readline
def main():
    N = int( input())
    for _ in range(N):
        n = int( input())//2
        print(n*(n+1)*(2*n+1)//3*4)
if __name__ == '__main__':
    main()
