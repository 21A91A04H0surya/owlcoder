class Solution:
    def clearDigits(self, s: str) -> str:
        stack=[]
        digi="1234567890"
        for i in s:
            if len(stack)==0 and i not in digi:
                stack.append(i)
            elif i in digi and len(stack)!=0:
                stack.pop()
            elif i not in digi:
                stack.append(i)
        return ''.join(stack)
            
                
        