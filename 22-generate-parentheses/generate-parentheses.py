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
        if r <l:
            st.append(')')
            self.para(l,r+1,n,st,ans)
            st.pop()
    def generateParenthesis(self, n: int) -> List[str]:
        l=0
        r=0
        st=[]
        ans=[]
        self.para(l,r,n,st,ans)
        return ans
        