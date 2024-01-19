#User function template for Python 3
import math
class Solution:
    def majorityElement(self,l,n):
        vo=0
        ca=0
        #Your code here
        for i in range(len(l)):
            if vo==0:
                ca=l[i]
                vo+=1
            else:
                if l[i]==ca:
                    vo+=1
                else:
                    vo-=1
        d=n//2
        c=0
        for i in l:
            if i == ca:
                c+=1
        if c>(n//2):
            return ca
        else:
            return -1
            
            
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

from sys import stdin


def main():
        T=int(input())
        while(T>0):
            
            N=int(input())

            A=[int(x) for x in input().strip().split()]
            
            
            obj = Solution()
            print(obj.majorityElement(A,N))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends