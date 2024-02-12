# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        c=0
        t=head
        temp=head
        while t != None:
            c+=1
            t=t.next
        d=0
        while temp!=None:
            if d == (c//2):
                return temp

            temp=temp.next
            d+=1

            
        
        
    


        