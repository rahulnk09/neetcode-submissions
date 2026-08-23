class Solution:

    def reversenode(self, start, end):
        prev, curr = None, start
        while curr != end:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev  # Returns new head of the reversed group

    def reverseKGroup(
        self, head: Optional[ListNode], k: int
    ) -> Optional[ListNode]:
        if not head or k == 1:
            return head

        dummy = ListNode(0)
        dummy.next = head
        group_prev = dummy

        while True:
            # Check if there are at least k nodes remaining
            kth = group_prev
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next

            group_next = kth.next
            start = group_prev.next

            # Reverse current group
            new_head = self.reversenode(start, group_next)

            # Re-link the reversed group back to the main list
            group_prev.next = new_head
            start.next = group_next

            # Move pointer to the end of the newly reversed group
            group_prev = start