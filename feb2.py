nm=input().split()
n=int(nm[0])
m=int(nm[1])
s=list(input())
a=list(map(int, input().split()))
c=a[:]

for M in range(m): 
    if s[0]=="L" and c[0]>0: c[n-1]+=1
    elif s[0]=="R" and c[0]>0: c[1]+=1
    if s[n-1]=="L" and c[n-1]>0: c[n-2]+=1
    elif s[n-1]=="R" and c[n-1]>0: c[0]+=1
    for i in range(1, n-1):
        if s[i]=="L" and c[i]>0: c[i-1]+=1
        elif s[i]=="R" and c[i]>0: c[i+1]+=1
    for i in range(n):
        if c[i]-1>a[i]: c[i]=a[i]
        elif c[i]>0: c[i]-=1
        
print(sum(c))