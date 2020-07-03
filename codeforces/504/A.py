N, K = map( int, input().split())
S = input()
L = 0
for i in range(1,N):
    if S[i:] == S[:N-i]:
        L=N-i
        break
part = S[L:]
S += part*(K-1)
print(S)
