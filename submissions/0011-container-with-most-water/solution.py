class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Start 2 pointers at max width
        # Move pointer pending on which is smallest until they reach the middle
        # then work out width * height to determine current max
        # currmax overrides res until pointers meet.
        max_area = 0
        l, r = 0, len(heights) -1
        while l < r:
            width = r - l
            curr_height = min((heights[l], heights[r]))
            max_area = max(max_area,curr_height * width)
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1

        return max_area
