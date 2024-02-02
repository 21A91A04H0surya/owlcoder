#User function Template for python3

class Solution:
    def perm(self,s,n,stri,ans,freq):
        if len(stri)==n:
            ans.append(stri)
            return
        for i in range(len(s)):
            if freq[i]==0:
                freq[i]=1
                self.perm(s,n,stri+s[i],ans,freq)
                freq[i]=0
    def permutation(self,s):
        n=len(s)
        ans=[]
        freq=[0]*n
        self.perm(s,n,"",ans,freq)
        ans.sort()
        return ans
    
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    T=int(input())
    while(T>0):
        s=input()
        ob=Solution()
        ans=ob.permutation(s)
        for i in ans:
            print(i,end=" ")
        print()
        
        T-=1
# } Driver Code Ends