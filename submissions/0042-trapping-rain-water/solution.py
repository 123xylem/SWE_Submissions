class Solution:
    def trap(self, height: List[int]) -> int:
        # Use 2 pointers. each pointer has a bottleneck of its prev max
        # We know its potential is gated by
        # PrevMax as the otherPointerMax is > current.
        # so we can just add pointerMax - currheight to res
        if not height:
            return 0
        l,r = 0, len(height) -1
        max_l = 0
        max_r = 0
        res = 0
        while l < r:
            if height[l] > height[r]:
                curr_area = max(0, max_r - height[r])
                max_r = max(max_r, height[r])
                res += curr_area
                r-=1
            else:
                curr_area = max(0, max_l - height[l])
                max_l = max(max_l, height[l])
                res += curr_area
                l+=1
        return res
