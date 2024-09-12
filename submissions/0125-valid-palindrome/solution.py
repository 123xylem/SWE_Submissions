class Solution:
    def isPalindrome(self, s: str) -> bool:
        #We make 2 pointers at start and end of string.
        # While they are moving we increment them if not alpahnum
        # When they are alphaNum we compare
        # if we get to the end with no false then its a palindrome
        l,r = 0, len(s) -1

        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while r > l and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False  
            l += 1
            r -= 1
        return True


