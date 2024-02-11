a=[int(x) for x in open('17_12471.txt')]
m13=0
for i in a:
    if i%100==13:
        m13=max(m13,i)
r=[]
for i in range(2,len(a)):
    if (a[i]%2==0) and(a[i-1]%2==0) and(a[i-2]%2==0) or\
       ((len(str(a[i]))==2)+(len(str(a[i-1]))==2)+(len(str(a[i-2]))==2))>=1:
            if a[i]+a[i-1]+a[i-2]<=m13:
                r+=[a[i]+a[i-1]+a[i-2]]
print(len(r),sum(r)//len(r))
                                                        

            
