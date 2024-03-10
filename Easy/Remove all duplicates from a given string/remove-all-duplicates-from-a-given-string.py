#User function Template for python3
from collections import Counter
class Solution:

	
	def removeDuplicates(self,s):
	    st=""
	    d={}
	    for i in s:
	        if i not in d:
	            st+=i
	            d[i]=1
	    return st
	            
	        
	        


#{ 
 # Driver Code Starts
#Initial Template for Python 3





if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        str = input().strip()
        ob = Solution()
        ans = ob.removeDuplicates(str)
        print(ans)
        tc -= 1

# } Driver Code Ends