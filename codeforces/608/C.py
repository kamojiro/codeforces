#import sys
#input = sys.stdin.readline
def main():
    n, sx, sy = map( int, input().split())
    S = [ tuple( map( int, input().split())) for _ in range(n)]
    ans = [0]*4
    for (x, y) in S:
        if x <= sx-1:
            ans[0] += 1
        elif x >= sx+1:
            ans[1] += 1
        if y <= sy-1:
            ans[2] += 1
        elif y >= sy+1:
            ans[3] += 1
    if sx == 0:
        ans[0] = -1
    elif sx == 10**9:
        ans[1] = -1
    if sy == 0:
        ans[2] = -1
    elif sy == 10**9:
        ans[3] = -1
    m = max(ans)
    print(m)
    point = [(sx-1, sy), (sx+1, sy), (sx, sy-1), (sx, sy+1)]
    for i in range(4):
        if ans[i] == m:
            print(point[i][0], point[i][1])
            break
if __name__ == '__main__':
    main()
