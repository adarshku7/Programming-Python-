# -*- coding: utf-8 -*-
"""
Created on Sat Jul 30 11:56:34 2022

@author: ADARSH
"""

def merge(intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort(key=KeySeconds)
        
        index=0
        
        for i in range(1,len(intervals)):
            
            if(intervals[index][1]>=intervals[i][0]):
                
                intervals[index][1]=max(intervals[i][1],intervals[index][1])
                
                
            else:
                
                index=index+1
                intervals[index]=intervals[i]
                
                
                
        return intervals[0:index+1]        
    
    
def KeySeconds(elem):
        
    return elem[0]



arr=[[1,3],[2,6],[8,10],[15,18]]
print(merge(arr))