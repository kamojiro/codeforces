#import sys
#input = sys.stdin.readline
def solve():
    n, m, k = map( int, input().split())
    if m == 0:
        return 0
    if n//k == 1:
        if m > 1:
            return 0
        else:
            return 1
    ans = 0
    for i in range(n//k, 0, -1):
        if i > m:
            continue
        if i > ((m-i)+(k-2))//(k-1) :
            if i - ((m-i)+(k-2))//(k-1) > ans:
                ans = i - ((m-i)+(k-2))//(k-1)
    return ans
    # if n//k + (n//k-1)*(k-1) < m:
    #     return 0
    # return min(n//k, )
def main():
    T = int( input())
    for _ in range(T):
        print(solve())
if __name__ == '__main__':
    main()

