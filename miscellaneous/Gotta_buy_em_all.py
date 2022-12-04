import math
i,s=input,sorted
t=int(i())
ai=lambda:list(map(int,i().split()))
p=lambda x:5*10**int(math.log10(x))
v=lambda x:x+p(x)-x%p(x)
while t:
    n,m=ai()
    a,b,t,x,k,j=s(ai()),s(ai()),t-1,1,0,0
    while j<n:
        if k<m and a[j]>=b[k]:
            if a[j]>v(b[k]):x=0
            k+=1
        j+=1
    print(["NO","YES"][x and k==m])