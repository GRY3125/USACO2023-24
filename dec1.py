a=input().split()
nlist=input().split()
mlist=input().split()
n=int(a[0])
m=int(a[1])

for x in range(m): 
    mlist[x]=int(mlist[x])
    original=mlist[x]
    candyleftover=mlist[x]
    for y in range(n): 
        if candyleftover>0:
            nlist[y]=int(nlist[y])
            if (original-candyleftover+1)<=nlist[y]: 
                if original>=nlist[y]:
                    aaa=nlist[y]-original+candyleftover
                    nlist[y]+=aaa
                    candyleftover-=aaa
                else: 
                    nlist[y]+=candyleftover
                    candyleftover=0
for x in nlist: 
    print(x)