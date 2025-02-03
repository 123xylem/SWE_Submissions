# We can dramatically reduce search time with 2 pointers
# get pointer mid point (l, r //2)
# Move mid point l or right pending on it being lower or higher then target
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) -1
        if nums[r] < target:
            return -1
        while l <= r:
            mid_point = l + r // 2
            if nums[mid_point] == target:
                return mid_point
            elif nums[mid_point] < target:
                l += 1
            else:
                r -= 1
        return -1

