# -*- coding: utf-8 -*-
"""
Created on Mon Aug  8 18:55:58 2022

@author: ADARSH
"""

def majorityElement(nums,k):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        unordered_map={}
        l=[]
        N=len(nums)
        x=N//k
        
        for i in range(N) :
            
            if nums[i] in unordered_map :
                
                unordered_map[nums[i]]+=1
                
                
            else:
                
                unordered_map[nums[i]]=1
                
                
        for k in unordered_map:
            
            
            if unordered_map[k] > x:
                
                l.append(k)
                
        return l 
    
    
    
    
arr = [ 1, 1, 2, 2, 3, 5, 4, 2, 2, 3, 1, 1, 1 ]    
k = 4
print(majorityElement(arr,k))
