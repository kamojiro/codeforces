import sys
input = sys.stdin.readline
from math import gcd
def main():
    t = int( input())
    ANS = []
    for _ in range(t):
        a, b, q = map( int, input().split())
        lr = [ tuple( map( int, input().split())) for _ in range(q)]
        lcm = a*b//gcd(a,b)
        G = []
        now = 0
        for i in range(lcm):
            if i%a%b != i%b%a:
                now += 1
            G.append(now)

        ans = []
        for l, r in lr:
            rans = r//lcm*now + G[r%lcm]
            lans = (l-1)//lcm*now + G[(l-1)%lcm]
            ans.append( rans - lans)

        ANS.append(ans)

    for ans in ANS:
        print(" ".join( map( str, ans)))
            
if __name__ == '__main__':
    main()
