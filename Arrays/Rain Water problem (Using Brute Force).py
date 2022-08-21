# -*- coding: utf-8 -*-
"""
Created on Sun Aug 21 19:24:01 2022

@author: ADARSH
"""

#using Brute Force 0(n^2)

def trappingWater(arr,n):
        #Code here
        
        res=0
    
        for i in range(1,n-1): #Running for index 1 to n-1
        
            left=arr[i]
        
            for j in range(i):
            
                left=max(left,arr[j])  #finding the largest wall one left side of current element
            
        
            right=arr[i]    
        
            for j in range(i+1,n):
            
                right=max(right,arr[j])  #finding the largest wall one right side of current element
            
        
            res= res + (min(left,right) - arr[i]) #Calculating the water filled for cuurent array
        
        
        
        return res  