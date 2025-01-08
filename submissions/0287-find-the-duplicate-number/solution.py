class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #This uses O(n) memory
        # Could use o(1) memory if I used floyd algo to find intersection with fast and slow
        # Then from that slow pointer create new slow pointer and both iterate until they land on duplicate
        tracker = {None: None}
        for num in nums:
            if num not in tracker:
                tracker[num] = 1
            else:
                return num
        return False
