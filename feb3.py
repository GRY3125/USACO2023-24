n, q = (int(x) for x in input().split())
c=list(map(int, input().split()))
t=list(map(int, input().split()))
vs=[tuple(map(int, input().split())) for _ in range(q)]
for x in range(n): 
    c[x]-=t[x]
for v,s in vs:
    if sum(i > s for i in c)<v: print("NO")
    else: print("YES")