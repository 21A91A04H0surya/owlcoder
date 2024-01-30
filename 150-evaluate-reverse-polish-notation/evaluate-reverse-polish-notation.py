class Solution:
    def evalRPN(self, t: List[str]) -> int:
        stack=[]
        s="+-/*"
        for i in t:
            if i not in s:
                stack.append(i)
            if i in s:
                d=eval(stack[-2]+i+stack[-1])
                stack.pop()
                stack.pop()
                stack.append(str(int(d)))
        return int(stack[0])


        