class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # 2 maps of have and need characters
        # on exact match of chars we can increment have value by one
        # Once have value = need value we can get length of window.
        # we can pop the left of window until have != need
        # Then we increment again.
        # return value is smallest valid window length
        if len(t) > len(s):
            return ""
        target_chars = {}
        have_chars = {}
        for a in t:
            target_chars[a] = target_chars.get(a, 0) +1

        have, need = 0, len(set(target_chars))
        res = float('inf')
        res_string = ''

        l = 0
        for r in range(len(s)):
            if s[r] in target_chars:
                have_chars[s[r]] = have_chars.get(s[r], 0) + 1
                if have_chars[s[r]] == target_chars[s[r]]:
                    have += 1
                    # print(f'have {have} {have_chars}, tmap: {target_chars} need: {need}')
                # Once match found record length 
                # Then pop the left off for potential smaller match
                while have == need:
                    length = (r - l) + 1
                    if length < res:
                        res = length
                        res_string = s[l:r+1]
                        # print(res_string, r, l)
                    if s[l] in have_chars and have_chars[s[l]] > 0:
                        have_chars[s[l]] -= 1
                    if s[l] in have_chars and have_chars[s[l]] < target_chars[s[l]]:
                        have -= 1
                    l += 1

        return res_string



