#User function Template for python3
import math
class Solution:
    def primeProduct (self, n):
        # code here
        ans=1
        l=[]
        while n%2==0:
            if n%2==0 and 2 not in l:
                l.append(2)
            n=n//2
        for i in range(3,int(math.sqrt(n))+1,2):
            while n%i==0:
                if i not in l:
                    
                    l.append(i)
                n=n//i
        if n>2 and n not in l:
            l.append(n)
        for i in l:
            ans=ans*i
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
       

        ob = Solution()
        print(ob.primeProduct(N))
# } Driver Code Ends