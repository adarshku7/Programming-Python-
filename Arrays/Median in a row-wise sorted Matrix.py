# -*- coding: utf-8 -*-
"""
Created on Sat Sep  3 13:20:32 2022

@author: ADARSH
"""

import heapq
def median(matrix, r, c):
    	#code here 
    	
    	res=matrix[0]
    	heapq.heapify(res)
    	
    	
    	for i in range(1,r):
    	    
    	    for j in range(c) :
    	        
    	        heapq.heappush(res,matrix[i][j])
    	        
    	        
    	x=heapq.nsmallest(r*c,res)
    	y=len(x)//2
    	return x[y]