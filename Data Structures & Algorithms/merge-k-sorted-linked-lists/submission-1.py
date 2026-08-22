# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dh = node = ListNode()
        c1, c2 = l1, l2

        while c1 and c2:
            if c1.val < c2.val:
                node.next = c1
                c1 = c1.next
            else:
                node.next = c2
                c2 = c2.next
            node = node.next

        node.next = c1 if c1 else c2
        return dh.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Edge Cases: empty list input or lists with empty nodes
        if not lists or len(lists) == 0:
            return None

        # Divide and Conquer approach (O(N log k))
        while len(lists) > 1:
            merged_lists = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                merged_lists.append(self.mergeTwoLists(l1, l2))
            lists = merged_lists

        return lists[0]