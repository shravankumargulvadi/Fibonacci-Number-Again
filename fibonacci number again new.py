
# coding: utf-8

# In[10]:


import numpy as np
import sys
def fibn(n):
    

        a=np.random.randint(1, 100, n+1)
        a[0]=0
        if n>0:
            a[1]=1
    
        for i in range(2,n+1):
            
            a[i]=a[i-1]+a[i-2]
            a=np.float64(a)
        #print('I completed fibn \n')
        return(a[n])
def indexfinder(m):
    i=1
    a=0
    f=np.random.randint(1, 100, 2)
    f[0]=0
    f[1]=1
    while a!=1:
        f=np.float64(f)
        z=f[1]
        f[1]=f[0]+f[1]
        f[0]=z
        f[0]=f[0]%m
        f[1]=f[1]%m
        
        a=(f[0])+(f[1])
        a=np.float64(a)
        
        
        if a==1:
            #print('completed index \n')
            #print(i+1)
            return i+1
        else:
            i=i+1
            #print(i)
def seriesmaker(i, m):
    a=np.random.randint(1, 100, i)
    b=np.random.randint(1, 100, i)
    b[0]=0
    b[1]=1
    for i in range(i):
        if i>1:
            b[i]=b[i-1]%m+b[i-2]%m
        a[i]=b[i]%m
    return a 

def fibmod(p, m):
    i=indexfinder(m)
    k=p%i
    a=seriesmaker(i, m)
    return a[k]

if __name__ == '__main__':
    input_n = 2
    input_numbers = [int(x) for x in input().split()]
    print(fibmod(input_numbers[0],input_numbers[1]))
        

