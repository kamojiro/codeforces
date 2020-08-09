#import sys
#input = sys.stdin.readline
def main():
    for i in range(1,101):
        A = [j+1 for j in range(i)]
        for k in range(i):
            for l in range(k,i):
                t = 0
                for p in range(k, l+1):
                    t |= A[p]
                if t >= k-l+1:
                    continue
                else:
                    print(False)
                    break
        print(i)
if __name__ == '__main__':
    main()
