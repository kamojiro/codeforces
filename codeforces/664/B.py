def main():
    n, m , fx, fy = map( int, input().split())
    sx, sy = 1, fy
    ANS = []
    ANS.append((fx,fy))
    if fx != 1:
        ANS.append((sx,sy))
    for i in range(1, n+1):
        if i%2 == 1:
            for j in range(1,m+1):
                if (i == fx and j == fy) or (i == sx and j == fy):
                    continue
                ANS.append((i,j))
        else:
            for j in range(m,0,-1):
                if (i == fx and j == fy) or (i == sx and j == fy):
                    continue
                ANS.append((i,j))
    print("\n".join( [" ".join( map(str, ans)) for ans in ANS]))
            
if __name__ == '__main__':
    main()
