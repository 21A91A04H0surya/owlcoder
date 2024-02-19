#User function Template for python3
from collections import Counter
import heapq
class Solution:
    def minValue(self, s, k):
        # code here
        d=Counter(s)
        v=list(d.values())
        heap=[]
        for i in v:
            heapq.heappush(heap,-i)
        while k!=0:
            d=heapq.heappop(heap)
            d+=1
            heapq.heappush(heap,d)
            k-=1
        s=0
        for i in heap:
            s+=(i)*(i)
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