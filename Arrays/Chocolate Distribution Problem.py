# -*- coding: utf-8 -*-
"""
Created on Mon Aug 22 23:05:20 2022

@author: ADARSH
"""
#Sliding Window Technique


def findMinDiff(self, A,N,M):

        # code here
        
        A.sort()
        
        left=0
        right=M-1
        
        
        summ=A[N-1] - A[0]
        
        while(right<N):
            
            summ=min(summ, A[right]-A[left])
            
            left+=1
            right+=1
            
            
        return summ  