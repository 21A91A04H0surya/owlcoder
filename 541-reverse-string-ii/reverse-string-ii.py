class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        i=0
        st=""
        while i <= len(s):
            d=s[i:i+k]
            d=d[::-1]
            st+=d
            st+=(s[i+k:i+k+k])
            i+=k+k
        return st


        

        