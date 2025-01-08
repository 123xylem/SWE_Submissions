class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        tracker = {None: None}
        for num in nums:
            if num not in tracker:
                tracker[num] = 1
            else:
                return num
        return False
