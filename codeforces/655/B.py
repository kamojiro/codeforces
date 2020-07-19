#import sys
#input = sys.stdin.readline
def prime_factors(N): #素因数 1を含まないことに注意
    ret = []
    middle = int( N**(1/2))
    tmp = N
    for i in range(2, middle+1):
        if tmp%i == 0:
            while tmp%i == 0:
                tmp //= i
            ret.append(i)
    if tmp != 1:
        ret.append(tmp)
    return ret


def solve(n):
    if n == 2:
        return [1,1]
    p = sorted(prime_factors(n))[0]
    return [n//p,n//p*(p-1)]
def main():
    T = int( input())
    N = [ int( input()) for _ in range(T)]
    ANS = [" ".join( map( str, solve(n))) for n in N]
    print("\n".join( ANS))
if __name__ == '__main__':
    main()
