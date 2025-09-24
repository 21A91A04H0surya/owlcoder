class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack=[]
        for i in logs:
            if len(stack)==0 and i!="./" and i!="../":
                stack.append(i)
            else:
                if i=="../" and len(stack)!=0:
                    stack.pop()
                elif i!="./" and i!="../":
                    stack.append(i)
        return len(stack)

         
        