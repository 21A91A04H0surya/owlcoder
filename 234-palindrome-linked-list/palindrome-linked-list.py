# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        s=""
        temp=head
        while temp!=None:
            s+=str(temp.val)
            temp=temp.next
        s1=s[::-1]
        if s==s1:
            return True
        return False
        