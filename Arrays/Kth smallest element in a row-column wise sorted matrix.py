# -*- coding: utf-8 -*-
"""
Created on Sat Sep  3 12:54:07 2022

@author: ADARSH
"""
#Create an empty min heap using heapq in python.
#Now assign first row (list) in result variable and convert result list into min heap using heapify method.
#Now traverse remaining row elements and push them into created min heap.
#Now get k’th smallest element using nsmallest(k, iterable) method of heapq module.


import heapq
def kthSmallest(mat, n, k): 
    # Your code goes here
    
    
    res=mat[0]
    heapq.heapify(res)
    
    for i in mat[1:]:
    
        for ele in i :
        
             heapq.heappush(res,ele)
                

        
    res=heapq.nsmallest(k,res)
    
    return res[-1]