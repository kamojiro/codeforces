#import sys
#input = sys.stdin.readline
def main():
    A, B, C, D = map( int, input().split())
    ans = 0
    if B == C:
        for x in range(A,B+1):
            if x+B <= D:
                ans += x
            else:
                ans += D - B + 1
        print(ans)
        return
    for x in range(A, B+1):
        if C-x+1 >= B:
            if C+x <= D:
                ans += x*(x+1)//2
            else:
                ans += (D-C)*(D-C+1)//2
        else:
            if C+x <= D:
                ans += x*(x+1)//2 - (B-1)*B//2
            else:
                if B <= D-x:
                    ans += (D-C)*(D-C+1)//2 - (B-1)*B//2
                        
        if B <= D-x+1 <= C:
            ans += (D-C+1)*(C-D+x)
            
        # if C < D-x+1:
        #     if B <= C-x+1:
        #         ans += x*(x+1)//2
        #     else:
        #         ans += x*(x+1)//2 - B*(B-1)//2
        #     continue
        # else:
        #     if C-x+1 < B:
                
        #     if B <= C-x+1:
        #         ans += (D-C)*(D-C+1)//2
        #     else:
        #         ans += (D-C)*(D-C+1)//2 - B*(B-1)//2
        # if B <= D-x+1:
        #     ans += (D-C+1)*(C-D+x)
        # else:
        #     ans += (D-C+1)*(C-B+1)
    print(ans)
if __name__ == '__main__':
    main()
