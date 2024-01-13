#User function Template for python3

import math
class Solution:
	def AllPrimeFactors(self, n):
		# Code here
		l=[]
		while n%2==0:
		    if n%2==0:
		        if 2 not in l:
		            l.append(2)
		        n=n//2
	    for i in range(3,int(math.sqrt(n))+1,2):
	        while n%i==0:
	            if i not in l:
	                l.append(i)
	            n=n//i
        if n>2:
    	   if n not in l:
    	       l.append(n)
        return l
		    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		N = int(input())
		ob = Solution()
		ans = ob.AllPrimeFactors(N)
		for _ in ans:
			print(_, end = " ")
		print()
# } Driver Code Ends