import sys
input = sys.stdin.readline
def main():
    N = int( input())
    for _ in range(N):
        n, m = map( int, input().split())
        if n == 1:
            print(0)
        elif n == 2:
            print(m)
        else:
            print(m*2)
if __name__ == '__main__':
    main()





