# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        first,second=ListNode(-1,head),head
        i=1

        while i!=(n+1):
            i+=1
            second=second.next
        
        while second:
            second=second.next
            first=first.next

        if first.next==head:
            return head.next
        else:
            first.next=first.next.next
            return head

