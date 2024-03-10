def codee():
    n=int(input())
    h=input().split()
    a=input().split()
    t=input().split()
    counter=0
    achieve=0
    while counter<10 and achieve==0:
        orderh=[]
        for x in h:
            orderh.append(int(x))
        orderh.sort()
        yn=1
        for x in range(n): 
            if int(orderh[int(t[x])])!=int(h[x]): 
                yn=0
        for x in range(n):
            h[x]=int(h[x])+int(a[x])
        if yn==1: 
            achieve=1 
    return counter           
        
        

ttt=int(input())
for x in range(ttt): 
    wow=codee()
    print(wow)