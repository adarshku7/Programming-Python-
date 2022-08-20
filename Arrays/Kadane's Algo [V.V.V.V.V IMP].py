#User function Template for python3



#for all cases except when all array elements are -ve
def maxSubArraySum(self,arr,N):
        ##Your code here
        
        
        
        sum=0
        maxsum=arr[0]
        
        for i in range(N):
            sum=sum+arr[i]
            
            if(sum<0):
                sum=0
            
            if(maxsum<sum):
                
                maxsum=sum

        return maxsum




#for all cases
def maxSubArraySum(self,arr,N):
        ##Your code here
        
        
       sumed=arr[0]
       maxsum=arr[0]
       
       for i in range(1,N):
           
           sumed=max(arr[i],arr[i]+sumed)
           maxsum=max(maxsum,sumed)
           
       return maxsum   