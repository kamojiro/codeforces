t = int( input())
for _ in range(t):
    L, v, l, r = map( int, input().split())
    print(L//v + (l-1)//v - r//v)
