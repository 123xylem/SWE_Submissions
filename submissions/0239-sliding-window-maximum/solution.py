class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Store indicies of largest in window
        # Store largest one in window popping all smaller
        # Once R is window length (k) we pop the left most item from window
        # The remaining nums will only be the largest in the window 
        # append that to output array and run the loop again. 
        largest_num = []
        l,r = 0, 0
        temp_arr = []

        while r < len(nums):
            while temp_arr and nums[r] > nums[temp_arr[-1]]:
                temp_arr.pop()
            temp_arr.append(r)

            if l > temp_arr[0]:
                temp_arr.pop(0)

            if (r + 1) >= k:
                largest_num.append(nums[temp_arr[0]])
                l += 1 
            r+=1
        return largest_num
        #Brute force:
        #Iterate through array taking max of range each time

        #
        # for r in range(k-1, len(nums)):
        #     print(nums[l], nums[r], nums[l:r+1:1])
        #     largest_num.append(max(nums[l:r+1:1]))
        #     l+=1
        # return largest_num
