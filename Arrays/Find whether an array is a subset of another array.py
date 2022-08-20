# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 15:43:41 2022

@author: ADARSH
"""

#User function Template for python3

#Important : Array of elements can be repeated 
#example a1= [1,2,3,4,5,6,7,8]
#a2=[1,3,5,1]

def isSubset( a1, a2, n, m):
    
    
    mp = {} #HashMap
    for i in range(n):
        if(a1[i] not in mp):
            mp[a1[i]] = 1
        else:
            mp[a1[i]] += 1
    
    for i in range(m):
        if(a2[i] not in mp or mp[a2[i]]==0):
            return "No"
        else:
            mp[a2[i]] -= 1
    
    return "Yes"