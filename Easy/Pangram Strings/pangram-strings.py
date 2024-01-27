#User function Template for python3
class Solution:
	def isPanagram(self, S):
		# code here
		c=0
		s=S.lower()
		v="abcdefghijklmnopqrstuvwxyz"
		for i in v:
		    if i in s:
		        c+=1
	    if c==26:
	        return 1
	    else:
	        return 0


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		S = input()
		ob = Solution()
		answer = ob.isPanagram(S)
		print(answer)

# } Driver Code Ends