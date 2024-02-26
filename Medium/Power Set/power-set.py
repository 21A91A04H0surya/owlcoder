#User function Template for python3

class Solution:
	def AllPossibleStrings(self, s):
		# Code here
		res=[]
		for i in range(2**(len(s))):
		    o=[]
		    for j in range(len(s)):
		        if i >> j & 1 > 0:
		            o.append(s[j])
		    if len(o)!=0:
		        res.append(''.join(o))
		    
		res.sort()
	    return res
		


#{ 
 # Driver Code Starts

#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s = input()
		ob = Solution();
		ans = ob.AllPossibleStrings(s)
		for i in ans:
			print(i, end = " ");
		print()
# } Driver Code Ends