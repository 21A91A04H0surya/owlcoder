#User function Template for python3

class Solution:
    def printperm(self,s,stri,n,ans,freq):
        if len(stri)==n:
            ans.append(stri)
            return
        for i in range(len(s)):
            if freq[i]==0:
                freq[i]=1
                self.printperm(s,stri+s[i],n,ans,freq)
                freq[i]=0
        
    def find_permutation(self, s):
        # Code here
        ans=[]
        n=len(s)
        freq=[0]*n
        
        self.printperm(s,"",n,ans,freq)
        return list(set(ans))
        



#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__':
	t=int(input())
	for i in range(t):
		S=input()
		ob = Solution()
		ans = ob.find_permutation(S)
		ans.sort()
		for i in ans:
			print(i,end=" ")
		print()
# } Driver Code Ends