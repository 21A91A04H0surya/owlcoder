#User function Template for python3

import math
class Solution:
    def sumn(self,n):
        s=list(str(n))
        su=0
        for i in s:
            su+=int(i)
        return su
    def primfact(self,n):
        p=[]
        while n%2==0:
            p.append(2)
            n=n//2
        for i in range(3,int(math.sqrt(n))+1,2):
            while n%i==0:
                p.append(self.sumn(i))
                n=n//i
        if n > 2:
            p.append(self.sumn(n))
        if len(p)==1:
            return [0]
        else:
            return p
            
        
    def smithNum(self, n):
        # code here 
        d=self.primfact(n)
        sums=self.sumn(n)
        if sums==sum(d):
            return 1
        else:
            return 0


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n=int(input())
        
        ob = Solution()
        print(ob.smithNum(n))
# } Driver Code Ends