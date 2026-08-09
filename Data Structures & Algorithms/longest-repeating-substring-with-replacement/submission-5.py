class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if not s:
            return 0

        cf = [0] * 26
        l = 0
        res = 0
        max_freq = 0  # Track the maximum frequency dynamically
        
        for r in range(len(s)):
            char_idx = ord(s[r]) - ord('A')
            cf[char_idx] += 1
            
            # Update max_freq in O(1) instead of scanning the whole array
            max_freq = max(cf)
            
            # Window condition check
            if (r - l + 1) - max_freq > k:
                cf[ord(s[l]) - ord('A')] -= 1
                l += 1
            
            res = max(res, (r - l + 1))
            
        return res