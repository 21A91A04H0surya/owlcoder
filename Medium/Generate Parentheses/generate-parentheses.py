#User function Template for python3

class Solution:
    def para(self,l,r,n,st,ans):
        if l==n and r==n:
            a=st.copy()
            ans.append(''.join(a))
            return 
        if l < n:
            st.append('(')
            self.para(l+1,r,n,st,ans)
            st.pop()
        if r < l:
            st.append(')')
            self.para(l,r+1,n,st,ans)
            st.pop()
    def AllParenthesis(self,n):
        #code here
        st=[]
        ans=[]
        l=0
        r=0
        self.para(l,r,n,st,ans)
        # print(ans)
        return ans



#{ 
 # Driver Code Starts
#Initial Template for Python 3


        
if __name__=="__main__":
    t=int(input())
    for i in range(0,t):
        n=int(input())
        ob=Solution()
        result=ob.AllParenthesis(n)
        result.sort()
        for i in range(0,len(result)):
            print(result[i])
        

# } Driver Code Ends