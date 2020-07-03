#import sys
#input = sys.stdin.readline
def solve():
    n, x = map( int, input().split())
    adj = 0
    for _ in range(n-1):
        u, v = map( int, input().split())
        if u == x or v == x:
            adj += 1
    if adj <= 1:
        return "Ayush"
    if n%2 == 1:
        return "Ashish"
    else:
        return "Ayush"
def main():
    T = int( input())
    ANS = []
    for _ in range(T):
        ANS.append(solve())
    print("\n".join(ANS))
if __name__ == '__main__':
    main()
