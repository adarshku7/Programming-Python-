# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 15:46:05 2022

@author: ADARSH
"""

#Function to find if there exists a triplet in the 
    #array A[] which sums up to X.
    
    
#using Hashmap 0(n^2)    
    
def find3Numbers(self,A, n, X):
        # Your Code Here
        
        #Algorithm: 
        #Traverse the array from start to end. (loop counter i)
        #Create a HashMap or set to store unique pairs.
        #Run another loop from i+1 to end of the array. (loop counter j)
        #If there is an element in the set which is equal to x- arr[i] – arr[j], then print the triplet (arr[i], arr[j], x-arr[i]-arr[j]) and break
        #Insert the jth element in the set.
        
        
        for i in range(n-1):
            
            s=set()
            curr=X-A[i]
            
            for j in range(i+1,n):
                
                if(curr - A[j]) in s:   ##X-A[i]-A[j]
                    
                    return True
                    
                     
                     
                s.add(A[j])
            
        return False   