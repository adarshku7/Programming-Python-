# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 15:22:01 2022

@author: ADARSH
"""

#User function Template for python3

def rotate( arr, n):
    
   prev=arr[0]
   arr[0]=arr[n-1]
   curr=0
   
   for i in range(1,n):
       curr=arr[i]
       arr[i]=prev
       prev=curr

   return arr


#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        rotate(a, n)
        print(*a)

        T -= 1


if __name__ == "__main__":
    main()





    
# } Driver Code Ends