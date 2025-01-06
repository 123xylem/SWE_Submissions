#Track seen nodes in hashmap.
# if ever we see a node again we return true
# Else false.

#Memory optimised solution uses slow/fast pointer. IF fast ever = slow twice then theres been a loop
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        node_tracker = {}
        while head:
            if head in node_tracker:
                return True
            else:
              node_tracker[head] = head.val
              head = head.next
        return False
