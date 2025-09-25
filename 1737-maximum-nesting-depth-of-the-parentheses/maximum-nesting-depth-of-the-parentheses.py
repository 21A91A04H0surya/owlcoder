class Solution:
    def maxDepth(self, s: str) -> int:
        stack=[]
        st="1234567890"
        m=0
        for i in s:
            if len(stack)==0 and(i in "()"):
                stack.append(i)
                
            else:
                if i=="(":
                    stack.append(i)
                    
                elif i==")":
                    m=max(m,len(stack))
                    stack.pop()
        return m
                    

                


        