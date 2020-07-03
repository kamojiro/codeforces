import sys
input = sys.stdin.readline
from collections import Counter
def main():
    T = int( input())
    for _ in range(T):
        S = list( map( int, list(input().strip())))
        N = len(S)
        C = Counter(S)
        if C[0] == N or C[0] == 0:
            print( "".join( map( str, S)))
            continue
        ans = [S[0]]
        for s in S[1:]:
            if ans[-1] == s:
                ans.append(s^1)
                ans.append(s)
            else:
                ans.append(s)
        print("".join( map( str, ans)))
        
if __name__ == '__main__':
    main()
