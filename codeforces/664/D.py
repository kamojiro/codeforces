#import sys
#input = sys.stdin.readline
from itertools import accumulate
def main():
    n, d, m = map( int, input().split())
    A = list( map( int, input().split()))
    A_low = []
    A_high = []
    for a in A:
        if a <= m:
            A_low.append(a)
        else:
            A_high.append(a)
    Ll = len(A_low)
    Lh = len(A_high)
    A_low.sort(reverse=True)
    A_high.sort(reverse=True)
    accA_high = [0] + list( accumulate(A_high))
    # print(accA_high)
    t = (n+d)//(d+1)
    if t <= Lh:
        ans = accA_high[(n+d)//(d+1)]
    else:
        ans = accA_high[-1]
    low = 0
    # print(ans)
    for i in range(Ll):
        low += A_low[i]
        t = (n-i-1+d)//(d+1)
        if t <= Lh:
            high = accA_high[(n-i-1+d)//(d+1)]
        else:
            high = accA_high[-1]
        # print(i, (n-i-1+d)//(d+1))
        # print(low, high)
        if low + high > ans:
            ans = low+high
    print(ans)
if __name__ == '__main__':
    main()
