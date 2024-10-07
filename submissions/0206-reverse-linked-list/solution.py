# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # init 2 pointers prev and curr
        # copy the currents Next Node into nxt(temp variable) 
        # Then we change currents nextNode to be the leftpointer
        # we iterate left pointer to current node 
        # We iterate value of curr to nxt (the next in list)
        # We return Prev which is now the head pointer and will point to all the other nodes in reverse.
        prev, curr = None, head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
    
        return prev


