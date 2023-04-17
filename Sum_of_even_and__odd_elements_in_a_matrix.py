r,c=map(int,input().split())
mat=[]
for i in range(r):
    s_l=list(map(int,input().split()))
    mat.extend(s_l)
ev=0
od=0
for i in mat:
    if i % 2 == 0:
        ev+=i
    else:
        od+=i
print(f'{ev} {od}')        
        
    