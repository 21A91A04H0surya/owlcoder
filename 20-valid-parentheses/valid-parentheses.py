class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        c=0
        if s[0] in '}])' or len(s)==1:
            return False
        else:
            for i in range(len(s)):
                if s[i] in '([{':
                    stack.append(s[i])
                else:
                    if s[i]==")" and len(stack)!=0 and stack[-1]=='(':
                        stack.pop()
                    elif s[i]=='}' and len(stack)!=0 and stack[-1]=='{':
                        stack.pop()
                    elif s[i]==']' and len(stack)!=0 and stack[-1]=='[':
                        stack.pop()
                    else:
                        c+=1
                        return False
        if len(stack)==0:
            return True
                                