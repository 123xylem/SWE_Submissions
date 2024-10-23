# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #Simply add to a new list the lowest of the 2 lists
        # Start with a dummy head_node
        # Copy it with tail node that will be used to build the list (and end as the tail)
        # Tail will = the smallest of the current list heads
        # Then we will increment the list and the tail
        # To deal with remainders we add whichever listnode is left
        head_node = ListNode()
        tail = head_node
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        if list1:
            tail.next = list1
                
        if list2:
            tail.next = list2
                       
        
        return head_node.next

