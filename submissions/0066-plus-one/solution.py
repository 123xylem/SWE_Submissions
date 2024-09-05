class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = ''.join(str(i) for i in digits)
        s = int(s) + 1
        s = str(s)
        return [int(x) for x in s]

