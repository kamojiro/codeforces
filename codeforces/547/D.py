n = int( input())
l = input()
r = input()
V = [[] for _ in range(27)]
ANS = [-1]*(n+1)
ans = 0
for i in range(n):
    if l[i] == "?":
        V[26].append(i+1)
    else:
        V[ ord(l[i]) - ord("a")].append(i+1)
rq = []
for i in range(n):
    if r[i] != "?":
        if V[ord(r[i]) - ord("a")]:
            # ANS.append( str(V[ord(r[i]) - ord("a")].pop(0)) + " " + str(i+1))
            ANS[V[ord(r[i]) - ord("a")].pop(0)] = i+1
            ans += 1
        elif V[26]:
            # ANS.append( str(V[26].pop(0)) + " " + str(i+1))
            ANS[V[26].pop(0)] = i+1
            ans += 1
    else:
        rq.append(i+1)
 
if rq:
    for i in range(27):
        while V[i] and rq:
            # ANS.append( str(V[i].pop(0)) + " " + str(rq.pop(0)))
            ANS[V[i].pop(0)] = rq.pop(0)
            ans += 1

# print( len(ANS))
print(ans)
# for s in ANS:
#     print(s)
for i in range(n+1):
    if not ANS[i] == -1:
        print( str(i) + " " + str(ANS[i]))
