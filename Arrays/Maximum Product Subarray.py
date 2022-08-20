
def MaxProd(arr,n):
    
    mi=ma=arr[0]
    res=0
    for i in range(1,n):
        
        if(arr[i]<0):
            ma,mi=mi,ma
            
        ma=max(arr[i],arr[i] * ma)
        mi=min(arr[i],arr[i] * mi)
        res=max(res,ma)
        #print(res)
        
        
    return res
    
    
    
N = 5
arr= [-2, -40, 0, -2, -3]  
print(MaxProd(arr,N))
    