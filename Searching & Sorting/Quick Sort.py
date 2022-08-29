# -*- coding: utf-8 -*-
"""
Created on Mon Aug 29 11:05:37 2022

@author: ADARSH
"""

#Quick Sort

def Quick_Sort(arr,p,r):
    
    if p<r :
        
        q=partition(arr,p,r)
        Quick_Sort(arr, p, q-1)
        Quick_Sort(arr, q+1, r)
        
        
        
        
def partition(arr,p,r):

   key=arr[r]
   i=p-1

   for j in range(p,r):

        if (key>=arr[j]):
            i+=1
            
            arr[j],arr[i]=arr[i],arr[j]
            
   arr[i+1],arr[r]=arr[r],arr[i+1] 

   return i+1   


#Driver Code
arr1=[9,6,5,0,8,2]
arr2=[13,19,9,5,12,8,7,4,21,2,6,11]

Quick_Sort(arr1,0,5)  
Quick_Sort(arr2,0,11)    
print(arr1)
print(arr2)
    
    
    
    
    