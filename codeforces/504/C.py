from copy import deepcopy
N = int( input())
A = [0]*N
B = [0]*N
M = -1
Ms = []
m = 3*(10**9)+1
ms = []
for i in range(N):
    a, b = map( int, input().split())
    A[i] = a
    B[i] = b
    if M == a:
        Ms.append(a)
    elif M < a:
        Ms = [i]
        M = a
    if m == b:
        ms.append(b)
    elif m > b:
        ms = [i]
        m = b
L = Ms + ms
ans = 0
for i in L:
    SA = deepcopy(A)
    SB = deepcopy(B)
    SA[i] = 0
    SB[i] = 10**9
    ans = max(ans, min(SB) - max(SA))
print(ans)
