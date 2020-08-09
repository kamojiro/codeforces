def solve():
    n, m = map( int, input().split())
    E = [[] for _ in range(n)]
    for _ in range(m):
        v, w = map( lambda x: int(x)-1, input().split())
        E[v].append(w)
        E[w].append(v)
    

def main():
    t = int( input())
    ANS = [solve() for _ in range(t)]
    print("\n".join( map( str, ANS)))
if __name__ == '__main__':
    main()
