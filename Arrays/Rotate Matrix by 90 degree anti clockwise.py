def rotateby90(a, n): 
        # code here
        #Done in Two steps
        #1. Sort each row in reverse
        #2. Transpose
        
        low=0
        high=0
        
        for i in range(n):
            
            low=0
            high=n-1
            
            while(low<high):
                
                 a[i][low],a[i][high]=a[i][high],a[i][low]
                 low+=1
                 high-=1
                 
        #print(a)         
                 
                 
        #Transpose
        
        for i in range(n):
            
            for j in range(i+1,n):
                
                a[i][j],a[j][i]=a[j][i],a[i][j]
                
                
        return a 