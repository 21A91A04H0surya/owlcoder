class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        st=""
        for i in range(len(word)):
            if word[i]!=ch:
                st+=word[i]
            else:
                st+=word[i]
                st=st[::-1]
                st+=word[i+1:]
                break
        return st
            
        