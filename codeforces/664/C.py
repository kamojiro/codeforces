#import sys
#input = sys.stdin.readline
from itertools import product
def main():
    n, m = map( int, input().split())
    A = list( map( int, input().split()))
    B = list( map( int, input().split()))
    AB = []
    for a in A:
        q = [a&b for b in B]
        AB.append(q)
    for i in range(n):
        AB[i].sort()
    G = []
    for i in range(9):
        t = 2**i
        R = [[ b&t == t for b in ab] for ab in AB]
        G.append(R)
    ans = 2**10
    for P in product( range(2), repeat=9):
        check = True
        now = 0
        for i in range(n):
            for j in range(m):
                for k in range(9):
                    if P[k] == 1:
                        pass
                    else:
                        if G[k][i][j]:
                            break
                else:
                    now |= AB[i][j]
                    break
            else:
                check = False
        if check:
            if now < ans:
                ans = now
    print(ans)
                
if __name__ == '__main__':
    main()
