# -*- coding: utf-8 -*-
"""
Created on Sat Aug  6 13:19:43 2022

@author: ADARSH
"""

def sumzero(arr,n):
    
    n_sum=0
    res=set()
    for i in range(0,n):
            
        n_sum=n_sum + arr[i]
            
        if(n_sum in res or n_sum==0): 
            return True
                    
        res.add(n_sum)        
   
    return False
        




n=4
arr=[4,2,-3,1,6]

print(sumzero(arr,n))        
            
            