class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        #Get match map by making array of counts for index of letters
        s1Map = [0] * 26
        s2Map = [0] * 26
        
        #init starting matches by getting count of letter index in s1 and 2
        for i in range(len(s1)):
            s1Map[ord(s1[i]) - ord("a")] += 1
            s2Map[ord(s2[i]) - ord("a")] += 1

        # Find matches by comparing s1 and s2. if 26 then all letter counts match and substring is found
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











        #This method starts window at first match and then loops to see if R finds whole substring
        #But too inefficient
        target = len(s1)  
        count = 0        
        required = {}
        
        for char in s1:
            required[char] = required.get(char, 0) + 1
        
        for l in range(len(s2)):
            temp_required = required.copy()  
            count = 0
            
            if s2[l] in temp_required and temp_required[s2[l]] > 0:
                temp_required[s2[l]] -= 1  
                count += 1  
                r = l + 1 
                if count == target:
                    return True
                while r < len(s2):
                    if s2[r] in temp_required and temp_required[s2[r]] > 0:
                        temp_required[s2[r]] -= 1 
                        count += 1  
                        if count == target:
                            return True
                    # If !char or is overused, break 
                    else:
                        break
                    r += 1
                
        
        return False

