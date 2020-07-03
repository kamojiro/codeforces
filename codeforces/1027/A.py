N = int( input())
for _ in range(N):
    ans = 'YES'
    T = int( input())
    S = input()
    S1 = list(S[:T//2])
    S2 = list(S[T//2:])
    S2 = S2[::-1]
    U1 = list( map( ord, S1))
    U2 = list( map( ord, S2))
    for i in range(T//2):
        if U1[i] == U2[i] or abs(U1[i]-U2[i]) == 2:
            pass
        else:
            ans = 'NO'
            break
    print(ans)
