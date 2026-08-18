# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1=l1
        n2=l2
        carry=0
        head=curr=ListNode
        multiplier=1
        while n1 or n2:
            val1=n1.val if n1 else 0
            val2=n2.val if n2 else 0

            val=(val1+val2+carry)%10
            carry=1 if (val1+val2+carry)>=10 else 0
            print(val,carry)
            curr.next=ListNode(val)

            curr=curr.next
            n1=n1.next if n1 else None
            n2=n2.next if n2 else None
        
        if carry:
            curr.next=ListNode(1)

        return head.next
        


        