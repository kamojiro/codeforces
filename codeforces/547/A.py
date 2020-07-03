n, m = map( int, input().split())
ans = 0
if m%n != 0:
    ans = -1
else:
    c = m//n
    while c%2 == 0:
        ans += 1
        c //= 2
    while c%3 == 0:
        ans += 1
        c //= 3
    if c != 1:
        ans = -1
print(ans)
