import sys
input = sys.stdin.readline
from collections import Counter
def solve():
    n, m = map( int, input().split())
    ans = 0
    for _ in range(n-1):
        t = input().strip()
        if t[-1] == "R":
            ans += 1
    ans += Counter( input())["D"]
    return ans
def main():
    t = int( input())
    ANS = [solve() for _ in range(t)]
    print("\n".join( map( str, ANS)))
if __name__ == '__main__':
    main()
