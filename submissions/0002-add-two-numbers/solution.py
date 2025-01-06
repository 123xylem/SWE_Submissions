class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #Make copy of list to build it and dummy as a reset to start
        # Add l1 +l2 each iteration
        # if more than 10 take surplus as current value
        # Make a carry for next iteration
        # use that carry as a node if l1,l2 finished
        dummy = ListNode()
        cur = dummy
        carry = 0

        while l1 or l2 or carry:

            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            # new digit
            val = v1 + v2 + carry
            carry = val // 10
            val = val % 10
            cur.next = ListNode(val)

            # update ptrs
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next
