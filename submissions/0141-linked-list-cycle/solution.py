class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        index_tracker = {}
        while head:
            if head in index_tracker:
                return True
            else:
              index_tracker[head] = head.val
              head = head.next
        return False
