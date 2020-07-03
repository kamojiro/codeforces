#import sys
#input = sys.stdin.readline
def solve():
    a, b = map( int, input().split())
    if a > b:
        a, b = b, a
    c = min(b-a,a)
    ans = c
    a -= c
    b -= c*2
    d = min(a,b)
    e = d//3
    ans += e*2
    a -= e*3
    b -= e*3
    if a >= 1 and b >= 2:
        ans += 1
        a -= 1
        b -= 2
    if a >= 2 and b >= 1:
        ans += 1
        a -= 1
        b -= 1
    return ans
    

def main():
    T = int( input())
    for _ in range(T):
        print(solve())
if __name__ == '__main__':
    main()
