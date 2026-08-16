# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        start=head
        N=0
        while start:
            N+=1
            start=start.next

        n=N-n+1
        if n==1:
            return head.next
        start=head
        
        c=1
        while start:
            if c==n-1:
                delnode=start.next
                next=delnode.next
                start.next=next
                break
            c+=1
            start=start.next
        return head