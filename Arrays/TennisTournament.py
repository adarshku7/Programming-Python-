#program to find maximum and minimum elements in an array
#Tennis Tournament Method

#driver code 

def MinMax(m,n,a):
    
    if m==n :
        a_max=a[m]
        a_min=a[n]
        
        return (a_max,a_min)
        
    elif n==m+1:
        if a[n]>a[m] :
            a_max=a[n]
            a_min=a[m]
            
        else:
            
            a_max=a[m]
            a_min=a[n]
            
        return (a_max,a_min)
            
            
    else:
        
        mid=int((m+n)/2)
        
        a_max1,a_min1=MinMax(m,mid,a)
        a_max2,a_min2=MinMax(mid+1,n,a)
        
        
    return (max(a_max1,a_max2),min(a_min1,a_min2)) 
    
    
        

a=[4,9,10,15,20,6,11,102,-3]
n=len(a)-1
m=0
Tmax,Tmin=MinMax(m,n,a)
print(Tmax,Tmin)


























#Driver code 

