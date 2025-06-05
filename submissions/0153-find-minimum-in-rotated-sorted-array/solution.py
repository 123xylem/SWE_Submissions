class Solution:
    def findMin(self, nums: List[int]) -> int:
        #Binary search.
        #Mid being more or less than r determines which half of list to search
        #Correct Pointer moves to mid to cut array in half
        #return l when l == r due to pointer convergence.
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if(nums[r] < nums[mid]):
                l = mid + 1
            else:
                r = mid
            print(nums[l],nums[mid], nums[r])

        return nums[l]
