# -*- coding: utf-8 -*-
"""
Created on Sat Aug  6 11:30:04 2022

@author: ADARSH
"""

def getPairsCount(arr, n, k):
        # code here
        #using hashing technqiue
        
        unordered_map={}
        count=0
        
        for i in range(n):
            
            if k-arr[i] in unordered_map:
                count+=unordered_map[k-arr[i]]
                
            if arr[i] in unordered_map:
                unordered_map[arr[i]]+=1
                
            else:
                
                unordered_map[arr[i]]=1
                
        print(unordered_map)        
                
                
        return count  




arr= [10, 12, 10, 15, -1, 7, 6, 5, 4, 2, 1, 1, 1]
sum = 11  
print(getPairsCount(arr,len(arr),sum))    
    