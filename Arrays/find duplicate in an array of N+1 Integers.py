# -*- coding: utf-8 -*-
"""
Created on Fri Jul 29 19:51:37 2022

@author: ADARSH
"""

def findDuplicate(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        x=len(nums)
        y=0
        
        for i in range(x):
            
            y=nums[i] % x
            nums[y]=nums[y]+x
            
        
        for j in range(x):
            
            if(nums[j]>=2*x):
                
                print(j,end=" ")
            
            
if __name__ == "__main__":   

         
    a = [1, 2, 3, 6, 3, 6, 1]   
    findDuplicate(a)      