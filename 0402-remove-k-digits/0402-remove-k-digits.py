class Solution:
    def removeKdigits(self, s: str, k: int) -> str:
        stack=[]
        c=k
        # code here
        if len(s) <k :
            return '0'
        else:
            for i in range(len(s)):
                if len(stack)==0:
                    stack.append(s[i])
                elif s[i] >= stack[-1]:
                    stack.append(s[i])
                else:
                    while True:
                        if c==0 or len(stack)==0 or stack[-1]<=s[i]:
                            break
                        if stack[-1]>s[i]:
                            stack.pop()
                            c-=1
                    stack.append(s[i])
            while c:
                stack.pop()
                c-=1
            st = "".join(stack).lstrip("0")
            if len(st)==0:
                return '0'
            else:
                return st
        