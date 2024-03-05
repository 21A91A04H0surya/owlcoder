#User function Template for python3

class Solution:
    #Complete this function
    # Function to find the maximum index difference.
    def maxIndexDiff(self,a, n): 
        minarr=[]
        maxarr=[]
        mini=999999999
        maxi=0
        c=0
        b=a.copy()
        b.reverse()
        for i in range(len(a)):
            minarr.append(min(a[i],mini))
            mini=minarr[-1]
        for i in range(len(b)):
            maxarr.append(max(b[i],maxi))
            maxi=maxarr[-1]
        maxarr.reverse()
        maxu=-1
        i=0
        j=0
        while i < n and j <n:
            if minarr[i]<=maxarr[j]:
                maxu=max(maxu,j-i)
                j+=1
            else:
                i+=1
                
        return maxu
                
            
            
                
    
    
                    
                
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            ob=Solution()
            print(ob.maxIndexDiff(arr,n))
            
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends