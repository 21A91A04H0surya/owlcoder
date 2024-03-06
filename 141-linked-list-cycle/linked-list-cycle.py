# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        ohead=head
        dic={}
        if head==None:
            return False
        
        while ohead.next!=None:
            if ohead.next not in dic:
                dic[ohead.next]=1
            elif ohead.next in dic:
                return True
            else:
                return False
            ohead=ohead.next

            
        