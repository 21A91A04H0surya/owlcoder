#User function Template for python3
class Solution:
    ##Complete this function
    #Function to rearrange  the array elements alternately.
    def rearrange(self,l, n): 
        ##Your code here
        o=[]
        i=0
        j=len(l)-1
        while True:
            if i==j:
                o.append(l[j])
                break
            if i>j:
                break
            o.append(l[j])
            o.append(l[i])
            i+=1
            j-=1
        l[::]=o[::]


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
            ob.rearrange(arr,n)
            
            for i in arr:
                print(i,end=" ")
            
            print()
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends