#import sys
#input = sys.stdin.readline
def main():
    n = int( input())
    S = list( input())
    b = 0
    w = 0
    T = [0]*n
    for i in range(n):
        if S[i] == 'B':
            b += 1
        else:
            w += 1
            T[i] = 1

    if b%2 == 1 and w%2 == 1:
        print(-1)
        return
    count = 0
    ans = []
    if b%2 == 1:
        for i in range(n-1):
            if T[i] == 0:
                continue
            T[i] = 0
            T[i+1] = 1-T[i+1]
            count += 1
            ans.append(i+1)
    else:
        for i in range(n-1):
            if T[i] == 1:
                continue
            T[i] = 1
            T[i+1] = 1-T[i+1]
            count += 1
            ans.append(i+1)

    print(count)
    if count == 0:
        return
    print(" ".join( map(str, ans)))

if __name__ == '__main__':
    main()
