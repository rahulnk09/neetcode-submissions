class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Quick edge case: s2 can't contain a permutation of s1 if it's shorter than s1
        if len(s1) > len(s2):
            return False

        cf = [0] * 26
        
        # Build the initial frequency map for s1
        for c in s1:
            cf[ord(c) - ord('a')] += 1
            
        l = 0
        
        for r in range(len(s2)):
            char_idx = ord(s2[r]) - ord('a')
            cf[char_idx] -= 1
            
            # FIX 1: If we have too many of the current character (count drops below 0),
            # slide the left pointer forward ONLY until we drop that extra character.
            while cf[char_idx] < 0:
                cf[ord(s2[l]) - ord('a')] += 1
                l += 1
                
            # FIX 2: Since the while loop above guarantees our window only contains 
            # valid characters, if the window size matches s1's length, it's a permutation.
            if (r - l + 1) == len(s1):
                return True
                
        return False