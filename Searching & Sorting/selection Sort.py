# -*- coding: utf-8 -*-
"""
Created on Mon Aug 29 12:22:49 2022

@author: ADARSH
"""

#Selection Sort (Priroirty Queue Sorting)
#minimum element will come to left after each iteration


def Insertion_Sort(arr):
    
    n=len(arr)
    mi=0
    
    for i in range(0,n-1):
        
        mi=i
        
        for j in range(i+1,n):
            
            if (arr[mi]>arr[j]):
                
                mi=j
                
        
        arr[mi],arr[i]=arr[i],arr[mi]
        
        
        
    return arr



#Driver Code
arr1=[9,6,5,0,8,2]
arr2=[13,19,9,5,12,8,7,4,21,2,6,11]

Insertion_Sort(arr1)  
Insertion_Sort(arr2)    
print(arr1)
print(arr2)    
                
        