# -*- coding: utf-8 -*-
"""
Created on Mon Aug 29 12:16:19 2022

@author: ADARSH
"""

#BubbleSort Algorith (Pairwise Algorithm)


def Bubble_Sort(arr):
    
    n=len(arr)
    flag=0
    
    for i in range(0,n): #after each itertation largest element goes to right
        flag=0
        
        for j in range(0,n-1-i):
            
            if(arr[j]>arr[j+1]):
                
                arr[j],arr[j+1]=arr[j+1],arr[j]
                flag=1
                
                
        if flag==0 :
            break
        
        
        
    return arr



#Driver Code
arr1=[9,6,5,0,8,2]
arr2=[13,19,9,5,12,8,7,4,21,2,6,11]

Bubble_Sort(arr1)  
Bubble_Sort(arr2)    
print(arr1)
print(arr2)
    