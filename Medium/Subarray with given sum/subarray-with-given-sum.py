#User function Template for python3

#Function to find a continuous sub-array which adds up to a given number.
class Solution:
    def subArraySum(self,l, n, s): 
       #Write your code here
       
        dic = {}
        for i in range(1,len(l)):
            l[i]=l[i]+l[i-1]
        for i in range(len(l)):
            if l[i]==s:
                return [1,i+1]
            if l[i]-s in dic:
                d=l[i]-s
                f=l.index(d)
                return [f+2,i+1]
            dic[l[i]] = 1
                
        return [-1]
                
        
        
           
           


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

def main():
        T=int(input())
        while(T>0):
            
            NS=input().strip().split()
            N=int(NS[0])
            S=int(NS[1])
            
            A=list(map(int,input().split()))
            ob=Solution()
            ans=ob.subArraySum(A, N, S)
            
            for i in ans:
                print(i, end=" ")
                
            print()
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends