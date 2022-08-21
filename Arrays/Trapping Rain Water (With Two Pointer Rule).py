# -*- coding: utf-8 -*-
"""
Created on Sun Aug 21 19:26:42 2022

@author: ADARSH
"""

def trappingWater(arr,n):
        #Code here
        
        left=0
        right=n-1
        res=0
        left_max=0
        right_max=0
        
        while(left<=right):

            
              
            if(left_max<=right_max):
                
                res=res+max(0,left_max-arr[left])
                
                left_max=max(left_max,arr[left])
                
                left+=1
                  
                  
                  
            else:
                
                res=res+max(0,right_max-arr[right])
                
                right_max=max(right_max,arr[right])
                
                
                right-=1
                
                  
        return res    
   