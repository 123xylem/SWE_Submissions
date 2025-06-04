class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        biggest_pile = max(piles)  
        l, r = 1, biggest_pile
        min_per_hour = biggest_pile 

        #Search mid eating speed to see if piles ate fast enough
        # if mid can then see how much slower we can go
        # r = mid - 1 
        # else speed up eating amount l = mid + 1
        if len(piles) == 1:
            return -(-piles[0] // h)
        while l <= r:
            mid = (l + r) // 2
            count = 0            
            for p in piles:
                count += -(-p // mid)
            if count > h:
                l = mid + 1
            else: #Update if loop completes
                min_per_hour = min(min_per_hour, mid)
                r = mid - 1
            
        return min_per_hour

