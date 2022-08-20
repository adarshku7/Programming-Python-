# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 23:21:02 2022

@author: ADARSH
"""

#Move all elements to one side of list


    
    
def Move(a,left,right):

    while(left<=right):
        
        #Case 1
        
        if(a[left]>0 and a[right]>0):
            
            right=right-1
            
        #Case 2
        
        elif(a[left]>0 and a[right]<0):
            
            a[left],a[right]=a[right],a[left]
            
            left=left+1
            right=right-1
            
        elif(a[left]<0 and a[right]<0):
            
            left+=1
            
        else:
            
            left=left+1
            right=right-1
            
            
a=[-12,11,-13,-5,6,-7,5,-3,-6]
print("Before Movement :",a)
Move(a,0,len(a)-1)
print("After Movement :",a)            

 




























