#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys


# } Driver Code Ends
#User function Template for python3

class Solution:
    def Combination_sum(self,fI,lI,ans,temp,tar,arr):
        if fI>=lI:
            if tar==0:
                c=temp.copy()
                ans.append(c)
            return
        
        '''pick'''
        if arr[fI] <= tar:
            temp.append(arr[fI])
            self.Combination_sum(fI,lI,ans,temp,tar-arr[fI],arr)
            temp.pop()
        '''non pick'''
        self.Combination_sum(fI+1,lI,ans,temp,tar,arr)
        
            
    
    #Function to return a list of indexes denoting the required 
    #combinations whose sum is equal to given number.
    def combinationalSum(self,arr,tar):
        first_index=0
        arr=list(set(arr))
        arr.sort()
        last_index=len(arr)
        ans=[]
        temp=[]
        self.Combination_sum(first_index,last_index,ans,temp,tar,arr)
        return ans
        
        
        
        
    
        # code here

#{ 
 # Driver Code Starts.


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        a = list(map(int,input().strip().split()))
        s = int(input())
        ob = Solution()
        result = ob.combinationalSum(a,s)
        if(not len(result)):
            print("Empty")
            continue
        for i in range(len(result)):
            print("(", end="")
            size = len(result[i])
            for j in range(size - 1):
                print(result[i][j], end=" ")
            if (size):
                print(result[i][size - 1], end=")")
            else:
                print(")", end="")
        print()

# } Driver Code Ends