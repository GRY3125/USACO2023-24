ii=input().split()
N=int(ii[0])
S=int(ii[1])
qi=[] # 1 if target
vi=[] # value of location
for x in range(N):
    ii=input().split()
    qi.append(int(ii[0]))
    vi.append(int(ii[1]))

direction=1 # 1 is right -1 is left
power=1

while S>0 and S<(N+1) and power!=0: 
    if qi[S-1]==0:
        power+=vi[S-1]
        direction*=-1
    elif qi[S-1]==1: 
        if power>=vi[S-1]: 
            qi[S-1]=2
    S+=power*direction

print(qi.count(2))