# -*- coding: utf-8 -*-
"""
Created on Mon Aug 29 13:25:06 2022

@author: ADARSH
"""

#BUILD HEAP (MAX)

# STEPS

#Traverse from non leaf node to root n//2 to 1
#Max Heapify at each iteration



def Max_heapify(arr,i,N):
    
    largest=i
    left=2*i + 1 
    right= 2*i + 2
    
    if (left<N and arr[left]>arr[largest]):
        
        largest=left
        
    if (right<N and arr[right]>arr[largest]):
        
        
        largest=right
        
        
        
    if largest!=i :

       arr[largest],arr[i]=arr[i],arr[largest]
       
       Max_heapify(arr,largest,N)
       

def Build_heap(arr,N):


    x=N//2
    
    for i in range(x,-1,-1):
        
        Max_heapify(arr,i,N)
        
        
def printHeap(arr,n):

    for i in range(N):

        print(arr[i],end=" ")         

# Driver Code
if __name__ == '__main__':
 
    # Binary Tree Representation
    # of input array
    #             1
    #           /    \
    #         3        5
    #       /  \     /  \
    #     4      6  13  10
    #    / \    / \
    #   9   8  15 17
    arr = [1, 3, 5, 4, 6, 13,
           10, 9, 8, 15, 17]
 
    N = len(arr)
    
    print("Before :",arr,end=" ")
    print("\n")
 
    Build_heap(arr, N)
   
    printHeap(arr, N)
 
    # Final Heap:
    #             17
    #           /    \
    #         15      13
    #        /  \     / \
    #       9     6  5   10
    #      / \   / \
    #     4   8 3   1





       