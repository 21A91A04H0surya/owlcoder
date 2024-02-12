# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fa=head
        sl=head
        while fa != None and fa.next != None:
            sl=sl.next
            fa=fa.next.next
        return sl

            
        
        
    


        