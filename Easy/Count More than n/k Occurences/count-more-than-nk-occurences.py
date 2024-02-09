#User function Template for python3
from collections import Counter

class Solution:
    
    #Function to find all elements in array that appear more than n/k times.
    def countOccurence(self,arr,n,k):
        c=0
        #Your code here
        dic=Counter(arr)
        for ke,v in dic.items():
            if v>(n//k):
                c+=1
        return c


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math



def main():
        T=int(input())
        while(T>0):
            
            N=int(input())

            A=list(map(int,input().split()))
            
            K=int(input())
            
            print(Solution().countOccurence(A, N, K))
            
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends