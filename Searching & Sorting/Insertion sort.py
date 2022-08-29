# -*- coding: utf-8 -*-
"""
Created on Sat Aug 27 22:02:21 2022

@author: ADARSH
"""



def Insertion_sort(arr):

    n=len(arr)
    
    
    for j in range(1,n):
        
        key=arr[j]
        i=j-1
        
        while i>=0 and arr[i]>key:
            
            arr[i+1]=arr[i]
            i=i-1
            
        arr[i+1]=key    
        
        
    return arr    
       
    
    
arr = [12, 11, 13, 5, 6]
print(Insertion_sort(arr))
  