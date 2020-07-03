#import sys
#input = sys.stdin.readline
from collections import Counter
def solve():
    n, x = map( int, input().split())
    A = Counter(list( map( lambda x: int(x)%2, input().split())))
    if A[0] == n:
        return("No")
    if A[0] > 0:
        if x < n:
            return("Yes")
        else:
            if A[1]%2 == 1:
                return("Yes")
            else:
                return("No")
    if x%2 == 1:
        return("Yes")
    else:
        return("No")
    

def main():
    T = int( input())
    ANS = []
    for _ in range(T):
        ANS.append(solve())
    print("\n".join(ANS))
if __name__ == '__main__':
    main()
