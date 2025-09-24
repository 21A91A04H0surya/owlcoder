class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1=[]
        stack2=[]
        for i in s:
            if len(stack1)==0 and i!='#':
                stack1.append(i)
            else:
                if i=='#':
                    if len(stack1)!=0:
                        stack1.pop()
                else:
                    stack1.append(i)
        for j in t:
            if len(stack2)==0 and j!='#':
                stack2.append(j)
            else:
                if j=='#':
                    if len(stack2)!=0:
                        stack2.pop()
                else:
                    stack2.append(j)
        # print(stack1,stack2)
        if ''.join(stack1)==''.join(stack2):
            return True
        return False
                
            

        