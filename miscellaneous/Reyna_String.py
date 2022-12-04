i=input
t=int(i())
o=ord
v=lambda c:26-o(c)+o('A')
while t:
    n,p=map(int,i().split())
    s=sorted(map(v,i()))
    ss,j,t=sum(s),0,t-1
    while j<n and ss>p:ss-=s[j];j+=1
    print(j-1)