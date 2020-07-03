N = int( input())
X = [ list( map( int, input().split())) for _ in range(N)]
X.sort(key = lambda x:x[1], reverse=True)
A = [X[0][0],X[0][1]]
B = [0,10**9]
for i in range(1, N):
    a, b = X[i]
    if max( A[1] - A[0], 0) > max( 0, min(B[1],b) - max(B[0],a)):
        B[0], B[1] = A[0], A[1]
    else:
        B[0] = max( B[0], a)
        B[1] = min( B[1], b)
    A = [ max(A[0], a), min(A[1], b)]
print( max(0, B[1] - B[0],A[1]-A[0]))
