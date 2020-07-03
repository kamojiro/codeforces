n = int( input())
A = list( map( int, input().split()))
f = 0
now = 0
t = 0
ans = 0
for i in range(n):
    if A[i] == 1:
        if t == 0:
            f += 1
        else:
            now += 1
    else:
        if t == 0:
            t = 1
        if now > 0:
            ans = max(now, ans)
            now = 0
print( max( ans, f+now))
