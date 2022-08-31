# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 15:07:30 2022

@author: ADARSH
"""

def solve(arr, n):
        # code here
        even=0
        odd=0
        
        arr.sort()
        
        for i in range(1,n,2):
            
            odd= str(odd) + str(arr[i])
            
        #print(int(odd))
            
        for j in range(0,n,2):
            
            even=str(even) + str(arr[j])
            
            
        #print(int(even))    
            
        return int(odd) + int(even)    