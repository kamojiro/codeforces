#import sys
#input = sys.stdin.readline
def eratosthenes(N):
    from collections import deque
    work = [True] * (N+1)
    work[0] = False
    work[1] = False
    ret = []
    for i in range(N+1):
        if work[i]:
            ret.append(i)
            for j in range(2* i, N+1, i):
                work[j] = False
    return ret

def main():
    t = int( input())
    A = [ int( input()) for _ in range(t)]
    K = 10**5
    Primes = eratosthenes(K)
    N = len(Primes)
    NearPrime= [False]*(K+1)
    for i in range(N):
        for f in Primes[i+1:]:
            e = Primes[i]
            if e*f > K:
                break
            NearPrime[e*f] = True
    # print(NearPrimes[:20])
    NearPrimes = []
    for i in range(K+1):
        if NearPrime[i]:
            NearPrimes.append(i)
    T = set()
    ST = [(0,0,0) for _ in range(101)]
    Z = 50
    for n in NearPrimes[:Z]:
        for m in NearPrimes[:Z]:
            if n == m:
                continue
            for k in NearPrimes[:Z]:
                if m == k or k == n:
                    continue
                T.add(n+m+k)
                if n+m+k <= 100:
                    ST[n+m+k] = (n,m,k)
                
    S = sorted(list(T))
    Under100 = [False]*101
    for s in S:
        if s > 100:
            break
        Under100[s] = True
    ANS = []
    # print(ST)
    no = "NO"
    yes = "YES"
    for a in A:
        if a <= 30:
            ANS.append(no)
            continue
        ANS.append(yes)
        ans = 0
        if a <= 100:
            for s in S:
                b = a-s
                p, q, r = ST[s]
                if p == b or b == q or b == r:
                    continue
                ans = (p,q,r,b)
                break
        else:
            ans = (a-30, 14,10,6)
        ANS.append(" ".join( map( str, ans)))
    print("\n".join(ANS))
                
            
    # print( len(T))
    # print( sorted(list(T)))
    # print(len(NearPrimes))
    
if __name__ == '__main__':
    main()
