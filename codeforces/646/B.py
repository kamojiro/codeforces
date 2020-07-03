from collections import Counter
def solve():
    S = input()
    C = Counter(S)
    ans = min(C["0"], C["1"])
    N = len(S)
    zerobef = 0
    onebef = 0
    zeroaf = C["0"]
    oneaf = C["1"]
    
    for s in S:
        if s == "0":
            zerobef += 1
            zeroaf -= 1
        else:
            onebef += 1
            oneaf -= 1
        now = min(zerobef+oneaf, onebef+zeroaf)
        if now < ans:
            ans = now
    return ans

def main():
    T = int( input())
    ANS = []
    for _ in range(T):
        ANS.append(solve())
    print("\n".join(map(str, ANS)))
if __name__ == '__main__':
    main()








