# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 22:42:25 2022

@author: ADARSH
"""




def PalinArray(arr ,n):
    # Code here
    
    for i in range(n):
        
        if(checkpalindrome(arr[i])):
            
            continue
        
        else:
            
            return False


    return True

def checkpalindrome(num):
    
    x=num
    rem=0
    sum=0
    
    
    while(x!=0):
        rem=x%10
        sum=sum*10 + rem
        x=x//10
        
        
    if (sum==num):
        
        return True
        
    else:
        
        return False