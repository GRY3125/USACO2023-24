import math
n=input()
a=input()
asplit=a.split("0")
asplit=list(filter(None, asplit))
b=[]
for x in asplit:
    b.append(len(x))
bsorted=b[:]
bsorted.sort()

if a[0]!="1" and a[-1]!="1":
    if b[0]%2==1:
        nights=(b[0]+1)/2
    else: 
        nights=b[0]/2
else: 
    if bsorted[0]==b[0] or bsorted[0]==b[-1]:
        c=bsorted[:]
        if len(b)!=1:
            if a[0]=="1":
                c.remove(b[0])
            if a[-1]=="1":
                c.remove(b[-1])
        if c[0]%2==1:
            tnights=(c[0]+1)/2
        else: 
            tnights=c[0]/2
        if tnights>=bsorted[0]:
            nights=bsorted[0]
        elif tnights<bsorted[0]:
            nights=tnights
    else: 
        if bsorted[0]%2==1:
            nights=(bsorted[0]+1)/2
        else: 
            nights=bsorted[0]/2
            
sum=0
for x in b:
    sum+=math.ceil(x/(nights*2-1))
    
print(sum)