class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        tracker = [] #[index, value]
        for i, num in enumerate(heights):
            start = i
            # When curr rect smaller then prev rect we want to see how big prev rect was
            # We pop off the stack and take prevRect vals = (num rects * rectHeight)
            # We then change the start index so that:
            # Current small rectanlge starts where their height was last plotted
            while tracker and tracker[-1][1] > num:
                idx, v = tracker.pop()
                area = (i - idx) * v
                if area > max_area:
                    max_area = area
                start = idx
            tracker.append([start, num])
        # Then we go through remaining rects (that havent been popped off/Completed)
        # We calc the area of these = height * number of them in stack
        for num in tracker:
            area = num[1] * (len(heights) - num[0])
            if area > max_area:
                max_area = area
        
        return max_area
