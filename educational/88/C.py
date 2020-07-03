import sys
input = sys.stdin.readline
def solve():
    h, c, t = map( int, input().split())
    if h <= t:
        return 1
    if 2*t <= h+c:
        return 2
    if 2*h+c <= t*3:
        if abs(2*h+c-t*3) >= (h-t)*3:
            return 1
        else:
            return 3
            
    l = 0
    r = 500000
    while r-l > 1:
        m = (l+r)//2
        if t*(2*m+1) < ((m+1)*h+m*c):
            l = m
        else:
            r = m
        # print(l,r)
    if abs(((l+1)*h+l*c)-t*(2*l+1))*(2*r+1) <= abs(((r+1)*h+r*c)-t*(2*r+1))*(2*l+1):
        return 2*l+1
    else:
        return 2*r+1

def main():
    T = int( input())
    for _ in range(T):
        print(solve())
if __name__ == '__main__':
    main()

#1000000 0 500001
