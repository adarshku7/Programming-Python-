# -*- coding: utf-8 -*-
"""
Created on Sat Aug  6 11:31:42 2022

@author: ADARSH
"""

#common element in three array using set

def commonElements (A, B, C, n1, n2, n3):
    
        uset1=set()
        uset2=set()
        uset3=set()
        
        for i in range(n1):
            uset1.add(A[i])
            
            
        for j in range(n2):
        
            uset2.add(B[j])
            
            
            
        for k in range(n3):
        
            if C[k] in uset1 and C[k] in uset2 :
            
                if C[k] not in uset3:
                
                    uset3.add(C[k]) 
                    
                    
        print(uset3)            
        return sorted(uset3)             
        
        
    
n1 = 6
A = [1, 5, 10, 20, 40, 80]
n2 = 5
B = [6, 7, 20, 80, 100]
n3 = 8
C = [3, 4, 15, 20, 30, 70, 80, 120]
k=commonElements(A,B,C,n1,n2,n3)
if(len(k)==0):
    print(-1)

for i in range(len(k)):
    
    print(k[i],end=" ")
    
    

