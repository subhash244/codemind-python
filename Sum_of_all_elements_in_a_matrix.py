r,c=map(int,input().split())
m=[]
for i in range(r):
    s_l=list(map(int,input().split()))
    m.append(sum(s_l)) 
print(sum(m))
    
    