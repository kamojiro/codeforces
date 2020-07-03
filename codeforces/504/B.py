N = int( input())
A = list( map( int, input().split()))
ans = 1
cnt = 0
now = 0
for i in range(N):
    if A[i] <= now*2:
        cnt += 1
    else:
        ans = max( ans, cnt)
        cnt = 1
    now = A[i]
ans = max(ans,cnt)
print(ans)
        









