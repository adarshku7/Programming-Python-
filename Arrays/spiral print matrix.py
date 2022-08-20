def spiralPrint(R, C, a):
    top=0
    left=0
    bottom=R-1
    right=C-1
    
    while(left<=right and top<=bottom):
 
    #printing left to right
        for i in range(left,right+1):
            print(a[top][i],end=" ")
        top+=1
 
    #printing top to bottom
        for i in range(top,bottom+1):
            print(a[i][right],end=" ")
        
        right=right-1
    
    
    #printing right to left
        if(top<=bottom):
            for i in range(right,left-1,-1):
                print(a[bottom][i],end=" ")
            bottom=bottom-1    
        
        if(left<=right):   
    #printing bottom to up 
            for i in range(bottom,top-1,-1):
                print(a[i][left],end=" ")
         
            left=left+1
    
    
    # Driver Code
a = [[4,6,0,2],
     [7,3,1,5],
     [7,7,8,4],
     [1,9,6,3],
     [4,6,0,2]]
 
R = 5
C = 4
 
# Function Call
spiralPrint(R, C, a)