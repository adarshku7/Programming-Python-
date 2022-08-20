#User function Template for python3
class Solution:
	def minJumps(self, arr, n):
	    #code here
	  if(arr[0]==0 and n>1):
	      return -1
	      
	  if(arr[0]==0 and n<=1):
	      
	      return 0
	   
	  res=0
	  far=0
	  curr=0
	  
	  for i in range(0,n-1):
	      
	      if(i+arr[i]>far):
	          far=i+arr[i]
	          
	      if(i==curr):
	          res+=1
	          curr=far
	          
      if(curr>=n-1):  # For example like [2,1,0,3]
       
          return res
          
      else:
          
          return -1
#{ 
#  Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		Arr = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.minJumps(Arr,n)
		print(ans)
# } Driver Code Ends