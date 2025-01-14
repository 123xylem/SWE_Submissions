class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Make working_ll (working List) and result_head(copy of working_ll with start reset )
        # Make 1 pointer for each list.
        # Compare pointers at each point 
        # take lowest val pointer and increment that list
        # Note curr Idx to be able to change correct list and validate a new num
        # When all internal lists are None we should have completed list.
        # We return the result_head.next which is the reset of our working_ll working LinkedList

        result_head = ListNode(None)
        working_ll = result_head
        pointers = [head for head in lists]

        while any(pointers):
            curr_smallest = ListNode(1001, None)
            curr_idx = -1
            for idx, num in enumerate(pointers):
                if num:
                    if curr_smallest.val > num.val:
                        curr_smallest = num
                        curr_idx = idx
                    # print(idx,  curr_smallest.val , num.val)
            if curr_idx != -1:
                working_ll.next = curr_smallest
                working_ll = working_ll.next
                # print(pointers[curr_idx].val, pointers[curr_idx].next)
                pointers[curr_idx] = pointers[curr_idx].next
                # print(f'INCREMENTED arr-{curr_idx} to {pointers[curr_idx].val if pointers[curr_idx] else None} ')
        return result_head.next





