#import sys
#input = sys.stdin.readline
def digit(n):
    t = list( map( int, list( str(n))))
    return max(t)*min(t)

def main():
    N = int( input())
    for i in range(100):
        N += digit(N)
        print(i+1, N)
if __name__ == '__main__':
    main()
