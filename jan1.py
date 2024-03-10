T=int(input())
Nlist=[]
cowslist=[]
for x in range(T): 
    Nlist.append(int(input()))
    cowslist.append(list(map(int, (input().split()))))

for w in range(T): # for every test case
    N=Nlist[w]
    cows=cowslist[w]
    maxx=cows[:]
    maxx.sort()
    max=maxx[-1]

    indexlist=[]
    for y in range(max): 
        indexlist.append([])
    for y in range(N): 
        indexlist[cows[y]-1].append(y)

    anslist=[]

    for x in range(len(indexlist)): 
        if len(indexlist[x])>1:
            yn=0
            for y in range(len(indexlist[x])-1):
                if yn==0:
                    for z in range(y+1, len(indexlist[x])): 
                        if yn==0:
                            a=indexlist[x][y]
                            b=indexlist[x][z]
                            if (b-a+1)<2*(z-y+1): 
                                anslist.append(x+1)
                                yn=1
    if len(anslist)>0:
        print(*anslist)
    else: 
        print(-1)