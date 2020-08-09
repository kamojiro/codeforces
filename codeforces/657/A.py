import sys
input = sys.stdin.readline
def solve():
    n = int( input())
    s = input().strip()
    t = "abacaba"
    ans = "No"
    for i in range(n-6):
        ANS = []
        check = True
        for j in range(n):
            if i <= j and j <= i+6:
                if s[j] == "?" or s[j] == t[j-i]:
                    ANS.append(t[j-i])
                else:
                    check = False
                    break
            else:
                if s[j] == "?":
                    ANS.append("x")
                else:
                    ANS.append(s[j])
        if not check:
            continue
        count = 1
        z = 0
        # print(i, ANS)
        for j in range(n-6):
            if j == i:
                continue
            for k in range(7):
                if ANS[j+k] != t[k]:
                    break
            else:
                count += 1
        # print(i, count)
        if count == 1:
            return "\n".join(["Yes", "".join(ANS)])
    return "No"

def main():
    T = int( input())
    ANS = [ solve() for _ in range(T)]
    print("\n".join(ANS))
if __name__ == '__main__':
    main()
