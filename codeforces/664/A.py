#import sys
#input = sys.stdin.readline

def solve():
    r, g, b, w = map( int, input().split())
    odd = 0
    RGB = [r,g,b]
    m = min(RGB)
    RGBW = [r, g, b, w]
    for x in RGBW:
        if x%2 == 1:
            odd += 1
    if odd == 0 or odd == 1 or odd == 4:
        return "Yes"
    if odd == 2:
        return "No"
    if odd == 3:
        if m > 0:
            return "Yes"
        else:
            return "No"
def main():
    t = int( input())
    ANS = [ solve() for _ in range(t)]
    print("\n".join( ANS))
if __name__ == '__main__':
    main()
