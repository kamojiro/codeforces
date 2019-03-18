from itertools import accumulate
n, r = map( int, input().split())
H = list( map( int, input().split()))
A = []
L = [0]*n
now = 0
ans = 0
# for i in range(r-1,0,-1):
#     if H[i] == 1:
#         V[i] = 1
#         for j in range(i,i+r):
#             L[i] = 1
#         break
# else:
#     ans = -1

for i in range(n):
    if i == now + r -1:
        if H[i] == 1:
            A.append(i)
        if not A:
            ans = -1
            break
        k = A[-1]
        A = []
        L[k] = 1
        now = k+r
        if now > n-1:
            break
    else:
        if H[i] == 1:
            A.append(i)
if now < n:
    if not A:
        ans = -1
    else:
        if A[-1]+r-1 < n-1:
            ans = -1
        else:
            L[A[-1]] = 1
now = 0
A = []
R = [0]*n
RH = H[::-1]

for i in range(n):
    if i == now + r -1:
        if RH[i] == 1:
            A.append(i)
        if not A:
            ans = -1
            break
        k = A[-1]
        A = []
        R[k] = 1
        now = k+r
        if now > n-1:
            break
    else:
        if RH[i] == 1:
            A.append(i)
if now < n:
    if not A:
        ans = -1
    else:
        if A[-1]+r-1 < n-1:
            ans = -1
        else:
            R[A[-1]] = 1
AR = list(accumulate(R))
now = 0
if ans == -1:
    print(-1)
else:
    ans = 10000
    now = 0
    ans = AR[-1]
    for i in range(n):
        if L[i] == 1:
            now += 1
            if i+r-1 < n-1:
                ans = min( ans, AR[-i-r+1]+now)
            else:
                ans = min(ans, now)
                print(ans)
