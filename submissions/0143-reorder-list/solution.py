class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #1.Find mid point with fast and slow pointer and seperate list in 2
        #2. Reverse end list order
        #3. merge start + end lists
        if not head or not head.next or not head.next.next:
            return
        #1
        # 2xFast and 1xSlow pointer 
        # Slow = mid point when fast is at end
        mid = end = head
        while end and end.next:
            end = end.next.next
            mid = mid.next
        
        #2. Reorder:
        #reverse 2nd half of list 
        p2 = mid
        prev = None
        while p2:
            p2.next, prev, p2 = prev, p2, p2.next
        
        # 3. Merge:
        #Set second to the last valid el of reversed end list
        first, second = head, prev
        while second.next:
            #save references
            first_next = first.next
            second_next = second.next
            
            #change nexts
            first.next = second
            second.next = first_next
            
            #increment nodes
            first = first_next
            second = second_next
     
