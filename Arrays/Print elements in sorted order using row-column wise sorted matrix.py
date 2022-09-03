# -*- coding: utf-8 -*-
"""
Created on Sat Sep  3 13:18:48 2022

@author: ADARSH
"""

import heapq
def sortedMatrix(N,Mat):
            #code here
            
        res=Mat[0]
        heapq.heapify(res)
            
        for i in Mat[1:]:
                
            for ele in i :
                    
                heapq.heappush(res,ele)
                    
                    
        x=heapq.nsmallest(N*N,res)
        
        #print(x)
        
        y=len(x)
        
        k=0
        for i in range(N):
            
            for j in range(N):
                
                Mat[i][j]=x[k]
                k+=1
        
        return Mat
        