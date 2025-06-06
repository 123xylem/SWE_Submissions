class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) -1

        while l <= r:
            mid = (l+r) // 2
            if nums[mid] == target:
              return mid

            #Start is lower half.
            if nums[l] <= nums[mid]:
                # If lower half doesnt contain target discount it by moving L halfway. 
                # Else Shorten it with R pointer
                if nums[mid] < target or nums[l] > target:
                    l = mid + 1
                else:
                    r = mid - 1
            else: #End is lower half Do opposite
                if nums[mid] > target or nums[r] < target:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1

