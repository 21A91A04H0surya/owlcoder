#User function Template for python3
from collections import Counter
class Solution:
    def minValue(self, s, k):
        # code here
        d=Counter(s)
        v=list(d.values())
        while k!=0:
            v.sort()
            for i in range(len(v)):
                v[-1]=v[-1]-1
                k-=1
                break
        s=0
        for i in v:
            s+=i*i
        return s
        
                    
                
        
                
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input()
        k = int(input())
        
        ob = Solution()
        print(ob.minValue(s, k))
# } Driver Code Ends