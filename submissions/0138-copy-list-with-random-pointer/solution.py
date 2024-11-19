# """
# # Definition for a Node.
# class Node:
#     def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
#         self.val = int(x)
#         self.next = next
#         self.random = random
# """
# from copy import deepcopy

# class Solution:
#     def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
#         dummy = deepcopy(head)

#         return dummy

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
# from copy import deepcopy

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        #Copy Head as dummy so we can traverse with a pointer & a restart start point
        # Make new_list and a copy for same reason
        # Make dict to store Node values during traverse - Init to none to avoid key error
        dummy = head
        new_list = Node(0)
        new_list_copy = new_list
        ran_dict = {None: None} 

        # while nodes - 
        # copy them with the new lists pointers .next prop (to keep reference to new_list intact) 
        # - we will eventually return new_list(HEAD)
        # Result NewList has all vals of head.
        # dict has all props of head
        while dummy:
            new_list_copy.next = Node(dummy.val)
            new_list_copy = new_list_copy.next
            ran_dict[dummy] = new_list_copy
            dummy = dummy.next

        #Reset Pointers to start
        dummy = head
        new_list_copy = new_list.next

        #Now add the random prop to newList found in the dict we just made
        while new_list_copy:
            new_list_copy.random = ran_dict[dummy.random]
            dummy = dummy.next
            new_list_copy = new_list_copy.next
        #return the head of newList 
        #(note new_list is 0 the next holds the first real node)
        return new_list.next
