class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Because list is sorted we can increase/decrease pointer pending on 
        # where we are from target
        # If too high we decrease x and vice versa
        i,x = 0, len(numbers) -1
        while i < x:
            if numbers[i] + numbers[x] > target:
                x -= 1
            if numbers[i] + numbers[x] < target:
                i += 1
            if numbers[i] + numbers[x] == target:
                return [i+1, x+1]
