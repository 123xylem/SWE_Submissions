class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Get substr of repeated chars by using k amount of replacements
        # Store values+frequencies of window in hashmap
        # While windowLength - mostFreq Count < k Replacements we have a valid window
        # Return biggest window
        l = 0
        res = 0
        count = {}
        most_freq = 0

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            most_freq = max(most_freq, count[s[r]])
            # if window size - mostFreq < k then we know we have a valid window 
            if (r - l) - most_freq < k:
                # Return the biggest window length
                res = max(res, (r - l) +1)
            else:
                #If window not valid move left up and remove its count from map
                count[s[l]] = count.get(s[l]) - 1
                l+=1
        return res
