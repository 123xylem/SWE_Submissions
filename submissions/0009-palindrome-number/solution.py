class Solution:
    def isPalindrome(self, x: int) -> bool:
        sx = str(x)
        for i in sx:
            if not i.isdigit():
                return False
        lx = list(sx)
        rev = lx.copy()
        rev.reverse()
        return lx == rev
