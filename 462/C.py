n = int( input())
X = list( map( int, input().split()))
ans = 0
X = sorted(X)
for i in range(n-1):
    ans += X[i]*(i+2)
ans += X[-1]*n
print(ans)
