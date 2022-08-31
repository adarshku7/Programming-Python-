# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 18:07:01 2022

@author: ADARSH
"""

def subArraySum(arr, n, s): 
       #Write your code here
       start=0
       summ=0
       #l=[]
       i=0
       
       if(s==0):
            
             #l.append(-1)    
             return [-1]
           
       
       
       for i in range(n):
           
            summ+=arr[i]
           
            while(summ>s):
               
               summ-=arr[start]
               start+=1
               
            if (summ==s):
                
                #l.append(start+1)
                #l.append(i+1)
               
               
                return [start+1,i+1]
            
            
                
       #l.append(-1)    
       return [-1]