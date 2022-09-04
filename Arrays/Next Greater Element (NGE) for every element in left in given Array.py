# -*- coding: utf-8 -*-
"""
Created on Sat Sep  3 16:23:05 2022

@author: ADARSH
"""


def createStack():
    
    stack=[]
    return stack


def SizeStack(stack):
    
    return len(stack)


def TopStack(stack):
    
    return stack[-1]

def isEmpty(stack):
    
    return len(stack)==0

def push(stack,x):
    
    stack.append(x)
    
    
def pop(stack):
    if isEmpty(stack):
        print("Error : stack underflow")
    else:
        return stack.pop()
    
    
def NGE(arr) :
    
    l=[]
    s=createStack()
    
    n=len(arr)
    
    for i in range(0,n):
        
        if(SizeStack(s)==0):
            
            l.append(-1)
            
        elif (SizeStack(s)>0 and arr[i]<TopStack(s)):
            
            l.append(TopStack(s))
            
            
        elif(SizeStack(s)>0 and arr[i]>=TopStack(s)): 
        
        
              while(SizeStack(s)>0 and arr[i]>=TopStack(s)):
                  
                     pop(s)
                  
                  
                  
              
              if(SizeStack(s)==0):
                  
                  l.append(-1)
                  
              else:
                  
                  l.append(TopStack(s))
                  
                  
        push(s,arr[i])            



       
    return  l

    





# Driver code
arr =[ 13 , 7, 6 , 12 ]
x=NGE(arr)    
print(x)    
    
    