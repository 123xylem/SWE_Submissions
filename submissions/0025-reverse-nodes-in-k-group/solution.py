# Helper funciton to get last node in K group iterates until k reached and returns it or Null to break the loop
# Reverse group ending at K
# Retain pointer for next group 
# Make first in this group use that pointer ^
# Update prevGroup to use the .next of the first node (^^ that pointer)

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        res = ListNode(0, head)
        prev_group = res
        while True:
            kth = self.getKth(prev_group, k)
            if not kth:
                break
            
            next_group = kth.next
            
            # Reverse K sized group pointers
            prev, curr = next_group, prev_group.next
            while curr != next_group:
                nxt = curr.next #pointer for nxt
                curr.next = prev #reverse next pointer 
                prev = curr #prev Pointer for next node
                curr = nxt  #increment current
            
            tmp = prev_group.next # pointer to original start Node of this group (which points to next group after reversal)
            prev_group.next = kth # Make pointer to last el
            prev_group = tmp #Point to reversed start Node

        return res.next

    def getKth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr

