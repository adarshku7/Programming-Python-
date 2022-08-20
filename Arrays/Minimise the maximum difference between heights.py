# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 15:23:12 2022

@author: ADARSH
"""

#User function Template for python3

class Solution:
    def getMinDiff(self, arr, n, k):
        # code here
        arr.sort()
        ans=arr[n-1] - arr[0]
        smallest=arr[0]+k
        largest=arr[n-1]-k
        mi=0
        ma=0
        
        for i in range(n-1):
            
            mi=min(smallest,arr[i+1]-k)
            ma=max(largest,arr[i]+k)
            if mi<0:
                continue
            
            ans=min(ans,ma-mi)
            
        return ans    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        k = int(input())
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.getMinDiff(arr, n, k)
        print(ans)
        tc -= 1

# } Driver Code Ends