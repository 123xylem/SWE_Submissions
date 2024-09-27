class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        # Get match maps by making array of counts ON the index of letters
        # init starting matches by getting count of letter index in s1 == s2
        # Find matches by using a window len(s1).
        # The l,r pointers will adjust matches based s1Map == s2Map at the l,r  ORD(index)
        #  if 26 matches are found then all letters are accounted for and its a match!

        s1Map = [0] * 26
        s2Map = [0] * 26
        
        for i in range(len(s1)):
            s1Map[ord(s1[i]) - ord("a")] += 1
            s2Map[ord(s2[i]) - ord("a")] += 1

        matches = 0
        for i in range(26):
            if s1Map[i] == s2Map[i]:
                matches +=1
            if matches == 26:
                return True

        # Use sliding window to see if [subString Length window] can increase matches to 26
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True

            idx = ord(s2[r]) - ord('a')
            s2Map[idx] += 1
            if s2Map[idx] == s1Map[idx]:
                matches += 1
            elif s2Map[idx] -1 == s1Map[idx]:
                matches -=1

            idx = ord(s2[l]) - ord('a')
            s2Map[idx] -= 1
            if s2Map[idx] == s1Map[idx]:
                matches += 1
            elif s2Map[idx] +1 == s1Map[idx]:
                matches -=1

            l+=1

        return matches == 26


