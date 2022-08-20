# -*- coding: utf-8 -*-
"""
Created on Wed Aug  3 19:15:21 2022

@author: ADARSH
"""


def nextPermutation(N, arr):
        
        
        
        i=j=N-1
        while (i>0 and arr[i-1]>=arr[i]):
            i-=1
            
        if(i==0):
            arr.reverse()
            return arr
            
        pivot=i-1
        
        while(arr[pivot]>=arr[j]):
            
            j-=1
            
        arr[pivot],arr[j]=arr[j],arr[pivot]
        
        l,r=pivot+1,N-1
        
        while l<r :
            arr[l],arr[r]=arr[r],arr[l]
            l+=1
            r-=1
            
        return arr    

            
            
arr=[3,1,5,1]
print(nextPermutation(len(arr),arr))            
            