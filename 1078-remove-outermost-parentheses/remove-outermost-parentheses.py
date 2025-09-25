class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack=[]
        ans=""
        for i in s:
            if len(stack)==0:
                stack.append(i)
            else:
                if i=="(":
                    stack.append(i)
                    ans+=i
                elif i==")" and len(stack)>1:
                    ans+=i
                    stack.pop()
                else:
                    stack.pop()
        return ans
