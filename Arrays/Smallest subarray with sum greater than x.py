# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 14:03:05 2022

@author: ADARSH
"""

def smallestSubWithSum( a, n, x):
        # Your code goes here 
        
        #sliding window property
        
        ans=n
        start=0
        summ=0
        
        
        for i in range(n):
            
            summ=summ + a[i]
            while(summ>x):
                
                summ-=a[start]
                ans = min (ans , i - start + 1)
                start=start+1
                
                
            
                
        return ans