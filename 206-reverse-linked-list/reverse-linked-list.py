# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp=head
        l=[]
        while temp!=None:
            l.append(temp.val)
            temp=temp.next
        l.reverse()
        if len(l)==0:
            return 
        heade=ListNode(l[0])
        headee=heade
        for i in range(1,len(l)):
            d=ListNode(l[i])
            heade.next=d
            heade=heade.next
        return headee