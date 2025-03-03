class MyStack:

    def __init__(self):
        self.stack=[]
        

    def push(self, x: int) -> None:
        self.stack.append(x)
        

    def pop(self) -> int:
        l_e=self.stack[-1]
        self.stack.pop()
        return l_e
        

    def top(self) -> int:
        top=self.stack[-1]
        return top
        

    def empty(self) -> bool:
        if len(self.stack)==0:
            return True
        return False

        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()