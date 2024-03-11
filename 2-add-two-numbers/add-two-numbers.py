# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        car=0
        c1=0
        c2=0
        temp1=l1
        temp2=l2
        while temp1!=None:
            c1+=1
            temp1=temp1.next
        while temp2!=None:
            c2+=1
            temp2=temp2.next
        if l1.val+l2.val>=10:
            x=(l1.val+l2.val)
            new_node=ListNode(x%10)
            x=x//10
            car=x%10       
        else:
            new_node=ListNode(l1.val+l2.val)
            car=0
        tem1=l1
        tem2=l2
        tem1=tem1.next
        tem2=tem2.next
        tata=new_node
        print()
        if c1>=c2:
            while tem2!=None:
                o=(tem1.val+tem2.val+car)
                if o>=10:
                    d=ListNode(o%10)
                    o=o//10
                    car=o%10
                    new_node.next=d

                else:
                    d=ListNode(o)
                    new_node.next=d
                    car=0
                tem1=tem1.next
                tem2=tem2.next
                new_node=new_node.next

            while tem1!=None:
                o=tem1.val+car
                if o>=10:
                    d=ListNode(o%10)
                    o=o//10
                    car=o%10                    
                    new_node.next=d
                else:
                    d=ListNode(o)
                    new_node.next=d
                    car=0
                tem1=tem1.next
                new_node=new_node.next
            print(car)
            if car!=0:
                d=ListNode(car)
                new_node.next=d
            return tata
        else:
            while tem1!=None:
                o=(tem1.val+tem2.val+car)
                if o>=10:
                    d=ListNode(o%10)
                    o=o//10
                    car=o%10
                    new_node.next=d

                else:
                    d=ListNode(o)
                    new_node.next=d
                    car=0
                tem1=tem1.next
                tem2=tem2.next
                new_node=new_node.next

            while tem2!=None:
                o=tem2.val+car
                if o>=10:
                    d=ListNode(o%10)
                    o=o//10
                    car=o%10                    
                    new_node.next=d
                else:
                    d=ListNode(o)
                    new_node.next=d
                    car=0
                tem2=tem2.next
                new_node=new_node.next
            print(car)
            if car!=0:
                d=ListNode(car)
                new_node.next=d
            return tata

        




        


                




        