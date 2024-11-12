class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if n == 0:
            return head
        # Create dummy to return start of new list
        # Slow begins when N iterations of Fast have hit
        # When Fast hits end Slow will be prev to Deletable Node
        # So just nextNext Slow and return dummy.next to point to start of slow
        dummy = ListNode(0, head)
        slow = dummy
        fast = head
        while n > 0:
            fast = fast.next
            n -= 1
        
        while fast:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next

        return dummy.next
