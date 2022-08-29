# -*- coding: utf-8 -*-
"""
Created on Mon Aug 29 15:53:42 2022

@author: ADARSH
"""
def Heap_sort(arr,N):
    

    
    m=[]
    for i in range(N-1,0,-1):
        arr[i],arr[0]=arr[0],arr[i]
        m.append(arr[i])
        N=N-1
        Max_heapify(arr,0,N)
        
    
    return m



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

    for i in range(n):

        print(arr[i],end=" ")  
        
        
    print("\n") 



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
    
    printHeap(arr, N)
 
    Build_heap(arr, N)
   
    printHeap(arr, N)
    
    m=Heap_sort(arr,N)
    
    printHeap(m, len(m))
 
    # Final Heap:
    #             17
    #           /    \
    #         15      13
    #        /  \     / \
    #       9     6  5   10
    #      / \   / \
    #     4   8 3   1

    
    
    
    