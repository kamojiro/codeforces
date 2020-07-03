#import sys
#input = sys.stdin.readline
def main():
    N = int( input())
    A = list( map( int, input().split()))
    cnt = 0
    for a in A:
        if a > 0:
            cnt += 1
    if cnt <= 1:
        print(0)
        return
    M = [0]*31
    for i in range(30,0,-1):
        m = 0
        now = 0
        diff = 0
        for a in A:
            if a > i:
                m = 0
                now = 0
                continue
            now += a
            if diff < now - m:
                diff = now - m
            if now < m:
                m = now
        M[i] = diff
    print( max([ M[i]-i for i in range(31)]))
if __name__ == '__main__':
    main()
