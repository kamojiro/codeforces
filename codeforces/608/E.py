#import sys
#input = sys.stdin.readline
def main():
    n, k = map( int, input().split())
    cnt = 1
    d = 0
    if n%2 == 0:
        d = 1
    if n == k:
        print(1)
        return
    while n >= 1:
        if cnt >= k:
            print(n)
            break
        if n%2 == 0:
            cnt += 1
            n //= 2
        else:
            cnt *= 2
            cnt += d
            n -= 1
if __name__ == '__main__':
    main()
