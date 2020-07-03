#import sys
#input = sys.stdin.readline
def main():
    a = int( input())
    b = int( input())
    c = int( input())
    d = int( input())
    e = int( input())
    f = int( input())
    ans1 = min(a, d)*e;
    if a < d:
        ans1 += min(d-a, min(b, c))*f
    ans2 = min(d, min(b, c))*f
    if min(d, min(b, c)) < d:
        ans2 += min(a, d - min(d, min(b, c)))*e
    ans = max(ans1, ans2);
    print(ans)

if __name__ == '__main__':
    main()
