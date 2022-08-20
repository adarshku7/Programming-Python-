# -*- coding: utf-8 -*-
"""
Created on Sat Aug  6 10:49:33 2022

@author: ADARSH
"""

def getPairsCount(arr, n, k):
        # code here
        #using hashing technqiue
        
        m=[0] * 1000000
        twice_count=0
        
        for i in range(0,n):
            
            m[arr[i]]+=1
        
        for i in range(0,n):
            
            twice_count+=m[k-arr[i]]  #duplicate will be added too [10,1,1,1] Total count=6 but it should be 3 
            
            if(k-arr[i]==arr[i]):
                
                twice_count-=1
                
                
        return int(twice_count/2)      
    
    
    
arr= [10, 12, 10, 15, -1, 7, 6, 5, 4, 2, 1, 1, 1]
sum = 11  
print(getPairsCount(arr,len(arr),sum))
